import datetime
from typing import Dict, List
from sqlmodel import Session, select
from fastapi import Depends
from inventory_service.models.dto.equipment import EquipmentType, Port, Slot
from inventory_service.models.response.equipment_response import EquipmentListResponse
from inventory_service.schemas.models.equipment import InventoryEquipment
from inventory_service.services.base_service import BaseService
from inventory_service.utils.mapper import Mapper
from inventory_service.config.database import get_session

class EquipmentService(BaseService[InventoryEquipment]):
    """Service class for Equipment inventory operations."""
    
    # Equipment type mapping from Autin to Granite categories
    # Based on the mapping table image provided
    EQUIPMENT_TYPE_MAPPING = {
        # Autin Category -> Granite Categories
        EquipmentType.DWDM: [EquipmentType.DWDM.value],
        EquipmentType.SDH: [EquipmentType.OTN.value, EquipmentType.SDH.value, EquipmentType.OPTICAL.value],
        EquipmentType.OLT: [EquipmentType.FTTM_MDU.value, EquipmentType.FTTH_OLT.value, EquipmentType.FTTH_ONT.value],
        EquipmentType.UPE: [EquipmentType.MBH.value, EquipmentType.ETHERNET_ACCESS.value],
        EquipmentType.DSLAM: [EquipmentType.DSLAM.value],  # Just DSLAM as requested
        EquipmentType.AGG: [EquipmentType.ETHERNET_AGGREGATOR.value],  # AGG maps to ETHERNET AGGREGATOR
        EquipmentType.MSAN: [EquipmentType.MSAN.value],
        EquipmentType.SWITCH: [EquipmentType.IP_SWITCH.value],
        EquipmentType.PE: [EquipmentType.PE_ROUTER.value],
        EquipmentType.RAN: [EquipmentType.RAN.value],
        EquipmentType.MW: [EquipmentType.MW_LINK.value, EquipmentType.MW_NODE.value],
    }
    
    def __init__(self, session: Session = Depends(get_session)):
        super().__init__(InventoryEquipment, session)

    async def get_equipment_by_type(
        self,
        equipment_type: EquipmentType,
        start_time: datetime,
        end_time: datetime
    ) -> EquipmentListResponse:
        """
        Get equipment by type and last modification timestamp range.
        
        Args:
            equipment_type: Equipment type from Autin category (EquipmentType enum)
            start_time: Start datetime for filtering
            end_time: End datetime for filtering
            
        Returns:
            EquipmentListResponse containing list of equipment
        """
        
        # Get the granite equipment types that map to the autin type
        granite_types = self.EQUIPMENT_TYPE_MAPPING.get(equipment_type, [])
        
        if not granite_types:
            # If no mapping found, return empty response
            return EquipmentListResponse(root=[])
        
        # Query database for equipment records with both datetime and equipment type filters
        stmt = select(InventoryEquipment).where(
            InventoryEquipment.last_mod_ts >= start_time,
            InventoryEquipment.last_mod_ts < end_time,
            InventoryEquipment.equipment_type.in_(granite_types)
        )
        
        result = self.session.exec(stmt)
        equipment_records = result.all()
        
        # Group records by equipment to create nested structure
        equipment_dict = self._group_equipment_records(equipment_records)
        
        # Convert grouped records to Equipment DTOs
        equipment_list = []
        for equipment_name, records in equipment_dict.items():
            # Use the first record for equipment-level info (like FTTX pattern)
            primary_record = records[0]
            equipment = Mapper.map_to_equipment(primary_record)
            
            # Now build the slots from all records for this equipment
            equipment.slots = self._build_slots_from_records(records)
            equipment_list.append(equipment)
        
        return EquipmentListResponse(root=equipment_list)
    
    def _group_equipment_records(self, records: List[InventoryEquipment]) -> Dict[str, List[InventoryEquipment]]:
        """
        Group equipment records by equipment name.
        
        Args:
            records: List of InventoryEquipment records
            
        Returns:
            Dictionary with equipment_name as key and list of records as value
        """
        equipment_dict = {}
        
        for record in records:
            equipment_name = record.equipment_name or "UNKNOWN"
            if equipment_name not in equipment_dict:
                equipment_dict[equipment_name] = []
            equipment_dict[equipment_name].append(record)
        
        return equipment_dict
    
    def _build_slots_from_records(self, records: List[InventoryEquipment]) -> List[Slot]:
        """
        Build slots and ports from equipment records.
        
        Args:
            records: List of InventoryEquipment records for one equipment
            
        Returns:
            List of Slot objects
        """
        slot_dict = {}
        
        for record in records:
            slot_no = record.slot_no or "N/A"
            
            if slot_no not in slot_dict:
                slot_dict[slot_no] = {
                    'record': record,
                    'ports': []
                }
            
            # Add port if port information exists
            if record.port_number:
                port = Port(
                    portNumber=record.port_number,
                    portStatus=record.port_status or "UNKNOWN"
                )
                slot_dict[slot_no]['ports'].append(port)
        
        # Create Slot objects
        slots = []
        for slot_no, slot_data in slot_dict.items():
            slot_record = slot_data['record']
            slot = Slot(
                slotNo=slot_no,
                cardType=slot_record.card_type or "UNKNOWN",
                cardStatus=slot_record.card_status or "UNKNOWN",
                ports=slot_data['ports']
            )
            slots.append(slot)
        
        return slots


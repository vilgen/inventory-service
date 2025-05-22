from datetime import datetime
from uuid import UUID
from inventory_service.models.dto.equipment import Equipment, EquipmentType, Port, Slot
from inventory_service.models.response.equipment_response import EquipmentListResponse


class EquipmentService:
    """
    Service for equipment-related operations.
    """

    async def get_equipment_list(
        self,
        equipment_type: EquipmentType,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> EquipmentListResponse:
        """
        Fetch equipment list based on type and time range.
        """
        # Mock implementation
        mock_port1 = Port(portNumber="00", portStatus="Available")
        mock_port2 = Port(portNumber="01", portStatus="Available")

        mock_slot1 = Slot(
            slotNo="02",
            cardType="IPMB",
            cardStatus="ASSIGNED",
            ports=[mock_port1]
        )

        mock_slot2 = Slot(
            slotNo="03",
            cardType="IPMB",
            cardStatus="ASSIGNED",
            ports=[mock_port2]
        )

        mock_equipment = Equipment(
            equipmentName=f"108-00-310-{equipment_type.value} MATB 1",
            shelfNumber="1",
            equipmentType=equipment_type.value,
            equipmentStatus="INSTALLED",
            equipmentVendor="HUAWEI",
            equipmentModel="UA5000",
            lastModifiedTime="18-APR-2023",
            inBandIP="10.11.10.1",
            siteNumber="101-00-000",
            siteCLLI="MURBRD00",
            slots=[mock_slot1, mock_slot2]
        )

        return EquipmentListResponse(root=[mock_equipment])
        
    async def get_equipment_list_with_mapping(
        self,
        equipment_type: EquipmentType,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID,
        use_mapping: bool = True
    ) -> EquipmentListResponse:
        """
        Fetch equipment list with Autin to Granite mapping applied.
        
        This method handles the mapping logic, calling get_equipment_list
        for each mapped equipment type.
        
        Args:
            equipment_type: EquipmentType enum member (Autin category)
            start_time: Start of time range
            end_time: End of time range
            client_msg_ref: Client message reference
            correlation_ref: Correlation reference
            use_mapping: Whether to apply the Autin->Granite mapping
            
        Returns:
            Combined EquipmentListResponse with equipment from all mapped types
        """
        # Mock implementation for multiple equipment types
        if not use_mapping:
            # If mapping is disabled, just return results for the original type
            return await self.get_equipment_list(
                equipment_type=equipment_type,
                start_time=start_time,
                end_time=end_time,
                client_msg_ref=client_msg_ref,
                correlation_ref=correlation_ref
            )
        
        # When mapping is enabled, generate results for each mapped type
        all_equipment = []
        
        # Get the Granite equipment types from the mapping
        granite_types = equipment_type.granite_names
        
        # Create mock equipment for each Granite type
        for granite_type in granite_types:
            mock_port1 = Port(portNumber="00", portStatus="Available")
            mock_port2 = Port(portNumber="01", portStatus="Available")

            mock_slot1 = Slot(
                slotNo="02",
                cardType="IPMB",
                cardStatus="ASSIGNED",
                ports=[mock_port1]
            )

            mock_slot2 = Slot(
                slotNo="03",
                cardType="IPMB",
                cardStatus="ASSIGNED",
                ports=[mock_port2]
            )

            mock_equipment = Equipment(
                equipmentName=f"108-00-310-{granite_type} MATB {granite_types.index(granite_type) + 1}",
                shelfNumber=str(granite_types.index(granite_type) + 1),
                equipmentType=granite_type,
                equipmentStatus="INSTALLED",
                equipmentVendor="HUAWEI",
                equipmentModel="UA5000",
                lastModifiedTime="18-APR-2023",
                inBandIP=f"10.11.10.{granite_types.index(granite_type) + 1}",
                siteNumber="101-00-000",
                siteCLLI="MURBRD00",
                slots=[mock_slot1, mock_slot2]
            )
            
            all_equipment.append(mock_equipment)
        
        return EquipmentListResponse(root=all_equipment)
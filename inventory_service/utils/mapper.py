from typing import List
from inventory_service.models.dto.circuit import Circuit
from inventory_service.models.dto.circuit_element import CircuitElement
from inventory_service.models.dto.copper import Copper
from inventory_service.models.dto.equipment import Equipment
from inventory_service.schemas.models.circuit import InventoryCircuit
from inventory_service.schemas.models.circuit_element import InventoryCircuitElement
from inventory_service.schemas.models.copper_service import InventoryCopperService
from inventory_service.schemas.models.equipment import InventoryEquipment
from inventory_service.schemas.models.fttx_service import InventoryFttxService
from inventory_service.models.dto.fttx import FTTHLinkInfo
from inventory_service.schemas.models.cross_connection import InventoryCrossConnection
from inventory_service.models.dto.cross_connection import CrossConnection
from inventory_service.models.dto.circuit_element import CircuitElementSequence

class Mapper:
    @staticmethod
    def safe_string(value) -> str:
        """Convert None values to empty string for safety"""
        return value if value is not None else ""
    
    @staticmethod
    def safe_list(value, delimiter=",") -> List[str]:
        """Convert string to list, handle None values"""
        if not value:
            return []
        return value.split(delimiter) if isinstance(value, str) else []
    
    @staticmethod
    def map_to_ftth_link_info(fttx_service: InventoryFttxService) -> FTTHLinkInfo:
        """Map InventoryFttxService to FTTHLinkInfo."""
        return FTTHLinkInfo(
            serviceID=Mapper.safe_string(fttx_service.service_id),
            serviceType=Mapper.safe_string(fttx_service.service_type),
            serviceStatus=Mapper.safe_string(fttx_service.service_status),
            TBNo=Mapper.safe_string(fttx_service.tb_no),
            TBCLLI=Mapper.safe_string(fttx_service.tb_clli),
            TBLattitude=Mapper.safe_string(fttx_service.tb_lattitude),
            TBLongitude=Mapper.safe_string(fttx_service.tb_longitude),
            TBPort=Mapper.safe_string(fttx_service.tb_port),
            TBOutputPort=Mapper.safe_string(fttx_service.tb_output_port),
            TBFreePorts=Mapper.safe_list(fttx_service.tb_free_ports),
            TBUtilizedPorts=Mapper.safe_list(fttx_service.tb_utilized_ports),
            FDTNo=Mapper.safe_string(fttx_service.fdt_no),
            FDTSPlitterNo=Mapper.safe_string(fttx_service.fdt_splitter_no),
            FDTCLLI=Mapper.safe_string(fttx_service.fdt_clli),
            FDTSPlitterOutputPort=Mapper.safe_string(fttx_service.fdt_splitter_output_port),
            FDTLattitude=Mapper.safe_string(fttx_service.fdt_lattitude),
            FDTLongitude=Mapper.safe_string(fttx_service.fdt_longitude),
            OLTName=Mapper.safe_string(fttx_service.olt_name),
            OLTModel=Mapper.safe_string(fttx_service.olt_model),
            OLTSLot=Mapper.safe_string(fttx_service.olt_slot),
            OLTUplinkPort=Mapper.safe_string(fttx_service.olt_uplink_port),  # Fixed
            OLTPONPort=Mapper.safe_string(fttx_service.olt_pon_port),
            OLTIP=Mapper.safe_string(fttx_service.olt_ip),
            OLTAggregator=Mapper.safe_string(fttx_service.olt_aggregator),
            OLTAggregatorIP=Mapper.safe_string(fttx_service.olt_aggregator_ip),
            OLTAggregatorPrimaryPort=Mapper.safe_string(fttx_service.olt_aggregator_primary_port),
            OLTAggregatorStandbyPort=Mapper.safe_string(fttx_service.olt_aggregator_standby_port),
            OLTDistrict=Mapper.safe_string(fttx_service.olt_district),
            OLTRegion=Mapper.safe_string(fttx_service.olt_region),
            OLTVendor=Mapper.safe_string(fttx_service.olt_vendor),
            OLTUpPort=Mapper.safe_string(fttx_service.olt_up_port),
            OLTSite=Mapper.safe_string(fttx_service.olt_site),
            ODFID=Mapper.safe_string(fttx_service.odf_id),  # Fixed
            ODFInputPort=Mapper.safe_string(fttx_service.odf_input_port),  # Fixed
            ODFOutputPort=Mapper.safe_string(fttx_service.odf_output_port),  # Fixed
            ONTSerialNumber=Mapper.safe_string(fttx_service.ont_serial_number),
            ONTModel=Mapper.safe_string(fttx_service.ont_model),
            ONTLastModifyDate=fttx_service.ont_last_modify_date.isoformat() if fttx_service.ont_last_modify_date else "",
            ONTID=Mapper.safe_string(fttx_service.ont_id),
            ONTDistrict=Mapper.safe_string(fttx_service.ont_district),
            ONTRegion=Mapper.safe_string(fttx_service.ont_region),
            ONTDownStreamBandwidth=Mapper.safe_string(fttx_service.ont_downstream_bandwidth),
            ONTUpStreamBandwidth=Mapper.safe_string(fttx_service.ont_upstream_bandwidth),
            businessUnit=Mapper.safe_string(fttx_service.business_unit),
            circuitPathName=Mapper.safe_string(fttx_service.circuit_path_name),
            EBUCircuitID=Mapper.safe_string(fttx_service.ebu_circuit_id),
            telephoneNumber=Mapper.safe_string(fttx_service.telephone_number)
        )
    
    @staticmethod
    def map_to_equipment(equipment_service: InventoryEquipment) -> Equipment:
        """Map InventoryEquipment to Equipment."""
        return Equipment(
            equipmentName=Mapper.safe_string(equipment_service.equipment_name),
            shelfNumber=Mapper.safe_string(equipment_service.shelf_number),
            equipmentType=Mapper.safe_string(equipment_service.equipment_type),
            equipmentStatus=Mapper.safe_string(equipment_service.status) or "UNKNOWN",
            equipmentVendor=Mapper.safe_string(equipment_service.equipment_vendor),
            equipmentModel=Mapper.safe_string(equipment_service.equipment_model),
            lastModifiedTime=equipment_service.last_modified_time.strftime("%d-%b-%Y") if equipment_service.last_modified_time else "",
            inBandIP=Mapper.safe_string(equipment_service.inband_ip),
            siteNumber=Mapper.safe_string(equipment_service.site_number),
            siteCLLI=Mapper.safe_string(equipment_service.site_clli),
            slots=[]  # Will be populated separately after grouping
        )
    
    @staticmethod
    def map_to_copper_service_info(copper_service: InventoryCopperService) -> Copper:
        """Map InventoryCopperService to Copper."""
        return Copper(
            pathname=Mapper.safe_string(copper_service.path_name),
            category=Mapper.safe_string(copper_service.category),
            
            # Voice equipment fields
            voiceEquipmentType=Mapper.safe_string(copper_service.voice_equipment_type),
            voiceExchangeID=Mapper.safe_string(copper_service.voice_exchange_id),
            voiceEquipmentCLLI=Mapper.safe_string(copper_service.voice_equipment_clli),
            voiceSlot=Mapper.safe_string(copper_service.voice_slot),
            voicePort=Mapper.safe_string(copper_service.voice_port),
            voiceAccessPortID=Mapper.safe_string(copper_service.voice_access_port_id),
            voiceEN=Mapper.safe_string(copper_service.voice_en),
            voiceNodeName=Mapper.safe_string(copper_service.voice_node_name),
            voiceNodeUpSlot=Mapper.safe_string(copper_service.voice_node_up_slot),
            voiceNodeUpPort=Mapper.safe_string(copper_service.voice_node_up_port),
            voiceNodeIPAddress=Mapper.safe_string(copper_service.voice_node_ip_address),
            voiceV5ID=Mapper.safe_string(copper_service.voice_v5_id),
            voiceSwitchID=Mapper.safe_string(copper_service.voice_switch_id),
            voiceHostExchangeSwitch=Mapper.safe_string(copper_service.voice_host_exchange_switch),
            voiceSwitchType=Mapper.safe_string(copper_service.voice_switch_type),
            voiceSwitchName=Mapper.safe_string(copper_service.voice_switch_name),
            voiceNMSJVCode=Mapper.safe_string(copper_service.voice_nms_jv_code),
            voiceSwitchModel=Mapper.safe_string(copper_service.voice_switch_model),
            voiceAggName=Mapper.safe_string(copper_service.voice_agg_name),
            voiceAggCLLI=Mapper.safe_string(copper_service.voice_agg_clli),
            voiceAggIP=Mapper.safe_string(copper_service.voice_agg_ip),
            voiceAggPrimaryPort=Mapper.safe_string(copper_service.voice_agg_primary_port),
            voiceAggStandbyPort=Mapper.safe_string(copper_service.voice_agg_standby_port),
            
            # Data equipment fields
            dataEquipmentType=Mapper.safe_string(copper_service.data_equipment_type),
            dataNodeName=Mapper.safe_string(copper_service.data_node_name),
            dataNodeUpSlot=Mapper.safe_string(copper_service.data_node_up_slot),
            dataNodeUpPort=Mapper.safe_string(copper_service.data_node_up_port),
            dataNodeIPAddress=Mapper.safe_string(copper_service.data_node_ip_address),
            dataEquipmentCLLI=Mapper.safe_string(copper_service.data_equipment_clli),
            dataSlot=Mapper.safe_string(copper_service.data_slot),
            dataPort=Mapper.safe_string(copper_service.data_port),
            dataAccessPortID=Mapper.safe_string(copper_service.data_access_port_id),
            dataEN=Mapper.safe_string(copper_service.data_en),
            dataEL=Mapper.safe_string(copper_service.data_el),
            
            # Copper cabinet fields
            copperCabinet=Mapper.safe_list(copper_service.copper_cabinet),
            cabinetStripPairDPPair=Mapper.safe_string(copper_service.cabinet_strip_pair_dp_pair),
            primaryStripCable=Mapper.safe_string(copper_service.primary_strip_cable),
            secondaryStripCable=Mapper.safe_string(copper_service.secondary_strip_cable),
            
            # Data switch fields
            dataV5ID=Mapper.safe_string(copper_service.data_v5_id),
            dataExchangeID=Mapper.safe_string(copper_service.data_exchange_id),
            dataHostExchangeSwitch=Mapper.safe_string(copper_service.data_host_exchange_switch),
            dataSwitchID=Mapper.safe_string(copper_service.data_switch_id),
            dataSwitchType=Mapper.safe_string(copper_service.data_switch_type),
            dataSwitchName=Mapper.safe_string(copper_service.data_switch_name),
            dataNMSJVCode=Mapper.safe_string(copper_service.data_nms_jv_code),
            dataAggName=Mapper.safe_string(copper_service.data_agg_name),
            dataAggCLLI=Mapper.safe_string(copper_service.data_agg_clli),
            dataAggIP=Mapper.safe_string(copper_service.data_agg_ip),
            dataAggPrimaryPort=Mapper.safe_string(copper_service.data_agg_primary_port),
            dataAggStandbyPort=Mapper.safe_string(copper_service.data_agg_standby_port),
            
            # Plate fields
            copperPlateID=Mapper.safe_string(copper_service.copper_plate_id),
            plateLatitude=Mapper.safe_string(copper_service.plate_latitude),
            plateIDLongitude=Mapper.safe_string(copper_service.plate_id_longitude),
            domainName=Mapper.safe_string(copper_service.domain_name),
            plateDistrict=Mapper.safe_string(copper_service.plate_district),
            plateRegion=Mapper.safe_string(copper_service.plate_region),
            plateExchange=Mapper.safe_string(copper_service.plate_exchange),
            treatmentPriority=Mapper.safe_string(copper_service.treatment_priority),
            
            # MDF fields
            MDFName=Mapper.safe_string(copper_service.mdf_name),
            MDFSlot=Mapper.safe_string(copper_service.mdf_slot),
            MDFPort=Mapper.safe_string(copper_service.mdf_port),
            classA=Mapper.safe_string(copper_service.class_a),
            telephoneNumber=Mapper.safe_string(copper_service.telephone_number)
        )

    @staticmethod
    def map_to_cross_connection(cross_connection: InventoryCrossConnection) -> CrossConnection:
        """Map InventoryCrossConnection to CrossConnection."""
        return CrossConnection(
            # A site fields
            aSiteEquipmentName=Mapper.safe_string(cross_connection.a_site_equipment_name),
            aSiteEquipmentType=Mapper.safe_string(cross_connection.a_site_equipment_type),
            aSiteEquipmentVendor=Mapper.safe_string(cross_connection.a_site_equipment_vendor),
            aSiteCTPId=Mapper.safe_string(cross_connection.a_site_ctp_id),
            aSiteShelf=Mapper.safe_string(cross_connection.a_site_shelf),
            aSiteSlot=Mapper.safe_string(cross_connection.a_site_slot),
            aSitePort=Mapper.safe_string(cross_connection.a_site_port),
            
            # Z site fields
            zSiteEquipmentName=Mapper.safe_string(cross_connection.z_site_equipment_name),
            zSiteEquipmentType=Mapper.safe_string(cross_connection.z_site_equipment_type),
            zSiteEquipmentVendor=Mapper.safe_string(cross_connection.z_site_equipment_vendor),
            zSiteCTPId=Mapper.safe_string(cross_connection.z_site_ctp_id),
            zSiteShelf=Mapper.safe_string(cross_connection.z_site_shelf),
            zSiteSlot=Mapper.safe_string(cross_connection.z_site_slot),
            zSitePort=Mapper.safe_string(cross_connection.z_site_port)
        )
    
    @staticmethod
    def map_to_circuit(circuit: InventoryCircuit) -> Circuit:
        """Map InventoryCircuit to Circuit."""
        return Circuit(
            name=Mapper.safe_string(circuit.name),
            revision=circuit.revision if circuit.revision is not None else 0,
            category=Mapper.safe_string(circuit.category),
            status=Mapper.safe_string(circuit.status),
            topology=Mapper.safe_string(circuit.topology),
            bandwidth=Mapper.safe_string(circuit.bandwidth),
            aSite=Mapper.safe_string(circuit.a_site),
            aNEType=Mapper.safe_string(circuit.a_ne_type),
            aNodeName=Mapper.safe_string(circuit.a_node_name),
            aPortBandwith=Mapper.safe_string(circuit.a_port_bandwidth),
            aPortName=Mapper.safe_string(circuit.a_port_name),
            aSlotNumber=Mapper.safe_string(circuit.a_slot_number),
            aShelfNumber=Mapper.safe_string(circuit.a_shelf_number),
            zSite=Mapper.safe_string(circuit.z_site),
            zNodeName=Mapper.safe_string(circuit.z_node_name),
            zNEType=Mapper.safe_string(circuit.z_ne_type),
            zPortBandwith=Mapper.safe_string(circuit.z_port_bandwidth),
            zPortName=Mapper.safe_string(circuit.z_port_name),
            zSlotNumber=Mapper.safe_string(circuit.z_slot_number),
            zShelfNumber=Mapper.safe_string(circuit.z_shelf_number)
        )
    
    @staticmethod
    def map_to_circuit_element(circuit_element: InventoryCircuitElement) -> CircuitElement:
        """Map InventoryCircuitElement to CircuitElement."""
        sequence = CircuitElementSequence(
            sequenceId=Mapper.safe_string(circuit_element.sequence_id),
            category=Mapper.safe_string(circuit_element.category),
            cardName=Mapper.safe_string(circuit_element.card_name),
            cardPort=Mapper.safe_string(circuit_element.card_port),
            cardDescription=Mapper.safe_string(circuit_element.card_description),
            portAccess=Mapper.safe_string(circuit_element.port_access),
            aSite=Mapper.safe_string(circuit_element.a_site),
            aNodeName=Mapper.safe_string(circuit_element.a_node_name),
            aNEType=Mapper.safe_string(circuit_element.a_ne_type),
            aPortBandwith=Mapper.safe_string(circuit_element.a_port_bandwidth),
            aPortName=Mapper.safe_string(circuit_element.a_port_name),
            aSlotNumber=Mapper.safe_string(circuit_element.a_slot_number),
            aShelfNumber=Mapper.safe_string(circuit_element.a_shelf_number),
            zSite=Mapper.safe_string(circuit_element.z_site),
            zNodeName=Mapper.safe_string(circuit_element.z_node_name),
            zNEType=Mapper.safe_string(circuit_element.z_ne_type),
            zPortBandwith=Mapper.safe_string(circuit_element.z_port_bandwidth),
            zPortName=Mapper.safe_string(circuit_element.z_port_name),
            zSlotNumber=Mapper.safe_string(circuit_element.z_slot_number),
            zShelfNumber=Mapper.safe_string(circuit_element.z_shelf_number),
            connectivity=Mapper.safe_string(circuit_element.connectivity)
        )
        
        return CircuitElement(
            circuitId=Mapper.safe_string(circuit_element.circuit_id),
            sequence=[sequence]
        )
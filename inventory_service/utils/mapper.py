from inventory_service.models.dto.circuit import Circuit
from inventory_service.models.dto.circuit_element import CircuitElement
from inventory_service.models.dto.copper import Copper
from inventory_service.schemas.models.circuit import InventoryCircuit
from inventory_service.schemas.models.circuit_element import InventoryCircuitElement
from inventory_service.schemas.models.copper_service import InventoryCopperService
from inventory_service.schemas.models.fttx_service import InventoryFttxService
from inventory_service.models.dto.fttx import FTTHLinkInfo
from inventory_service.schemas.models.cross_connection import InventoryCrossConnection
from inventory_service.models.dto.cross_connection import CrossConnection
from inventory_service.models.dto.circuit_element import CircuitElementSequence

class Mapper:
    @staticmethod
    def map_to_ftth_link_info(fttx_service: InventoryFttxService) -> FTTHLinkInfo:
        """Map InventoryFttxService to FTTHLinkInfo."""
        return FTTHLinkInfo(
            serviceID=fttx_service.service_id,
            serviceType=fttx_service.service_type,
            serviceStatus=fttx_service.service_status,
            TBNo=fttx_service.tb_no,
            TBCLLI=fttx_service.tb_clli,
            TBLattitude=fttx_service.tb_lattitude,
            TBLongitude=fttx_service.tb_longitude,
            TBPort=fttx_service.tb_port,
            TBOutputPort=fttx_service.tb_output_port,
            TBFreePorts=fttx_service.tb_free_ports.split(",") if fttx_service.tb_free_ports else [],
            TBUtilizedPorts=fttx_service.tb_utilized_ports.split(",") if fttx_service.tb_utilized_ports else [],
            FDTNo=fttx_service.fdt_no,
            FDTSPlitterNo=fttx_service.fdt_splitter_no,
            FDTCLLI=fttx_service.fdt_clli,
            FDTSPlitterOutputPort=fttx_service.fdt_splitter_output_port,
            FDTLattitude=fttx_service.fdt_lattitude,
            FDTLongitude=fttx_service.fdt_longitude,
            OLTName=fttx_service.olt_name,
            OLTModel=fttx_service.olt_model,
            OLTSLot=fttx_service.olt_slot,
            OLTUplinkPort=fttx_service.olt_uplink_port,
            OLTPONPort=fttx_service.olt_pon_port,
            OLTIP=fttx_service.olt_ip,
            OLTAggregator=fttx_service.olt_aggregator,
            OLTAggregatorIP=fttx_service.olt_aggregator_ip,
            OLTAggregatorPrimaryPort=fttx_service.olt_aggregator_primary_port,
            OLTAggregatorStandbyPort=fttx_service.olt_aggregator_standby_port,
            OLTDistrict=fttx_service.olt_district,
            OLTRegion=fttx_service.olt_region,
            OLTVendor=fttx_service.olt_vendor,
            OLTUpPort=fttx_service.olt_up_port,
            OLTSite=fttx_service.olt_site,
            ODFID=fttx_service.odf_id,
            ODFInputPort=fttx_service.odf_input_port,
            ODFOutputPort=fttx_service.odf_output_port,
            ONTSerialNumber=fttx_service.ont_serial_number,
            ONTModel=fttx_service.ont_model,
            ONTLastModifyDate=fttx_service.ont_last_modify_date.isoformat() if fttx_service.ont_last_modify_date else "",
            ONTID=fttx_service.ont_id,
            ONTDistrict=fttx_service.ont_district,
            ONTRegion=fttx_service.ont_region,
            ONTDownStreamBandwidth=fttx_service.ont_downstream_bandwidth,
            ONTUpStreamBandwidth=fttx_service.ont_upstream_bandwidth,
            businessUnit=fttx_service.business_unit,
            circuitPathName=fttx_service.circuit_path_name,
            EBUCircuitID=fttx_service.ebu_circuit_id,
            telephoneNumber=fttx_service.telephone_number
        )
    
    @staticmethod
    def map_to_copper_service_info(copper_service: InventoryCopperService) -> Copper:
        """Map InventoryCopperService to Copper."""
        return Copper(
            pathname=copper_service.path_name,
            category=copper_service.category,
            
            # Voice equipment fields
            voiceEquipmentType=copper_service.voice_equipment_type,
            voiceExchangeID=copper_service.voice_exchange_id,
            voiceEquipmentCLLI=copper_service.voice_equipment_clli,
            voiceSlot=copper_service.voice_slot,
            voicePort=copper_service.voice_port,
            voiceAccessPortID=copper_service.voice_access_port_id,
            voiceEN=copper_service.voice_en,
            voiceNodeName=copper_service.voice_node_name,
            voiceNodeUpSlot=copper_service.voice_node_up_slot,
            voiceNodeUpPort=copper_service.voice_node_up_port,
            voiceNodeIPAddress=copper_service.voice_node_ip_address,
            voiceV5ID=copper_service.voice_v5_id,
            voiceSwitchID=copper_service.voice_switch_id,
            voiceHostExchangeSwitch=copper_service.voice_host_exchange_switch,
            voiceSwitchType=copper_service.voice_switch_type,
            voiceSwitchName=copper_service.voice_switch_name,
            voiceNMSJVCode=copper_service.voice_nms_jv_code,
            voiceSwitchModel=copper_service.voice_switch_model,
            voiceAggName=copper_service.voice_agg_name,
            voiceAggCLLI=copper_service.voice_agg_clli,
            voiceAggIP=copper_service.voice_agg_ip,
            voiceAggPrimaryPort=copper_service.voice_agg_primary_port,
            voiceAggStandbyPort=copper_service.voice_agg_standby_port,
            
            # Data equipment fields
            dataEquipmentType=copper_service.data_equipment_type,
            dataNodeName=copper_service.data_node_name,
            dataNodeUpSlot=copper_service.data_node_up_slot,
            dataNodeUpPort=copper_service.data_node_up_port,
            dataNodeIPAddress=copper_service.data_node_ip_address,
            dataEquipmentCLLI=copper_service.data_equipment_clli,
            dataSlot=copper_service.data_slot,
            dataPort=copper_service.data_port,
            dataAccessPortID=copper_service.data_access_port_id,
            dataEN=copper_service.data_en,
            dataEL=copper_service.data_el,
            
            # Copper cabinet fields
            copperCabinet=copper_service.copper_cabinet.split(",") if copper_service.copper_cabinet else [],
            cabinetStripPairDPPair=copper_service.cabinet_strip_pair_dp_pair,
            primaryStripCable=copper_service.primary_strip_cable,
            secondaryStripCable=copper_service.secondary_strip_cable,
            
            # Data switch fields
            dataV5ID=copper_service.data_v5_id,
            dataExchangeID=copper_service.data_exchange_id,
            dataHostExchangeSwitch=copper_service.data_host_exchange_switch,
            dataSwitchID=copper_service.data_switch_id,
            dataSwitchType=copper_service.data_switch_type,
            dataSwitchName=copper_service.data_switch_name,
            dataNMSJVCode=copper_service.data_nms_jv_code,
            dataAggName=copper_service.data_agg_name,
            dataAggCLLI=copper_service.data_agg_clli,
            dataAggIP=copper_service.data_agg_ip,
            dataAggPrimaryPort=copper_service.data_agg_primary_port,
            dataAggStandbyPort=copper_service.data_agg_standby_port,
            
            # Plate fields
            copperPlateID=copper_service.copper_plate_id,
            plateLatitude=copper_service.plate_latitude,
            plateIDLongitude=copper_service.plate_id_longitude,
            domainName=copper_service.domain_name,
            plateDistrict=copper_service.plate_district,
            plateRegion=copper_service.plate_region,
            plateExchange=copper_service.plate_exchange,
            treatmentPriority=copper_service.treatment_priority,
            
            # MDF fields
            MDFName=copper_service.mdf_name,
            MDFSlot=copper_service.mdf_slot,
            MDFPort=copper_service.mdf_port,
            classA=copper_service.class_a,
            telephoneNumber=copper_service.telephone_number
        )

    @staticmethod
    def map_to_cross_connection(cross_connection: InventoryCrossConnection) -> CrossConnection:
        """Map InventoryCrossConnection to CrossConnection."""
        return CrossConnection(
            # A site fields
            aSiteEquipmentName=cross_connection.a_site_equipment_name,
            aSiteEquipmentType=cross_connection.a_site_equipment_type,
            aSiteEquipmentVendor=cross_connection.a_site_equipment_vendor,
            aSiteCTPId=cross_connection.a_site_ctp_id,
            aSiteShelf=cross_connection.a_site_shelf,
            aSiteSlot=cross_connection.a_site_slot,
            aSitePort=cross_connection.a_site_port,
            
            # Z site fields
            zSiteEquipmentName=cross_connection.z_site_equipment_name,
            zSiteEquipmentType=cross_connection.z_site_equipment_type,
            zSiteEquipmentVendor=cross_connection.z_site_equipment_vendor,
            zSiteCTPId=cross_connection.z_site_ctp_id,
            zSiteShelf=cross_connection.z_site_shelf,
            zSiteSlot=cross_connection.z_site_slot,
            zSitePort=cross_connection.z_site_port
        )
    
    @staticmethod
    def map_to_circuit(circuit: InventoryCircuit) -> Circuit:
        """Map InventoryCircuit to Circuit."""
        return Circuit(
            name=circuit.name, 
            revision=circuit.revision,
            category=circuit.category,
            status=circuit.status,
            topology=circuit.topology,
            bandwidth=circuit.bandwidth,
            aSite=circuit.a_site,
            aNEType=circuit.a_ne_type,
            aNodeName=circuit.a_node_name,
            aPortBandwith=circuit.a_port_bandwidth,
            aPortName=circuit.a_port_name,
            aSlotNumber=circuit.a_slot_number,
            aShelfNumber=circuit.a_shelf_number,
            zSite=circuit.z_site,
            zNodeName=circuit.z_node_name,
            zNEType=circuit.z_ne_type,
            zPortBandwith=circuit.z_port_bandwidth,
            zPortName=circuit.z_port_name,
            zSlotNumber=circuit.z_slot_number,
            zShelfNumber=circuit.z_shelf_number
        )
    
    @staticmethod
    def map_to_circuit_element(circuit_element: InventoryCircuitElement) -> CircuitElement:
        """Map InventoryCircuitElement to CircuitElement."""
        sequence = CircuitElementSequence(
            sequenceId=circuit_element.sequence_id,
            category=circuit_element.category or "",
            cardName=circuit_element.card_name or "",
            cardPort=circuit_element.card_port or "",
            cardDescription=circuit_element.card_description,
            portAccess=circuit_element.port_access,
            aSite=circuit_element.a_site or "",
            aNodeName=circuit_element.a_node_name,
            aNEType=circuit_element.a_ne_type,
            aPortBandwith=circuit_element.a_port_bandwidth,
            aPortName=circuit_element.a_port_name,
            aSlotNumber=circuit_element.a_slot_number or "",
            aShelfNumber=circuit_element.a_shelf_number or "",
            zSite=circuit_element.z_site or "",
            zNodeName=circuit_element.z_node_name,
            zNEType=circuit_element.z_ne_type,
            zPortBandwith=circuit_element.z_port_bandwidth,
            zPortName=circuit_element.z_port_name,
            zSlotNumber=circuit_element.z_slot_number or "",
            zShelfNumber=circuit_element.z_shelf_number or "",
            connectivity=circuit_element.connectivity
        )
        
        return CircuitElement(
            circuitId=circuit_element.circuit_id,
            sequence=[sequence]
        )
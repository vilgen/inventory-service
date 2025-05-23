from .base import SQLModel, Field, Optional, datetime

class InventoryCopperService(SQLModel, table=True):
    __tablename__ = "inventory_copper_service"

    # Primary key field
    id: int = Field(default=None, primary_key=True)  # Auto-incrementing primary key

    path_name: Optional[str] = Field(max_length=100)
    category: Optional[str] = Field(max_length=30)
    voice_equipment_type: Optional[str] = Field(max_length=30)
    voice_exchange_id: Optional[str] = Field(max_length=100)
    voice_equipment_clli: Optional[str] = Field(max_length=50)
    voice_slot: Optional[str] = Field(max_length=30)
    voice_port: Optional[str] = Field(max_length=50)
    voice_access_port_id: Optional[str] = Field(max_length=100)
    voice_en: Optional[str] = Field(max_length=3100)
    voice_node_name: Optional[str] = Field(max_length=3100)
    voice_node_up_slot: Optional[str] = Field(max_length=30)
    voice_node_up_port: Optional[str] = Field(max_length=50)
    voice_node_ip_address: Optional[str] = Field(max_length=3100)
    voice_v5_id: Optional[str] = Field(max_length=3100)
    voice_switch_id: Optional[str] = Field(max_length=3100)
    voice_host_exchange_switch: Optional[str] = Field(max_length=3100)
    voice_switch_type: Optional[str] = Field(max_length=3100)
    voice_switch_name: Optional[str] = Field(max_length=3100)
    voice_nms_jv_code: Optional[str] = Field(max_length=3100)
    voice_switch_model: Optional[str] = Field(max_length=3100)
    voice_agg_name: Optional[str] = Field(max_length=3100)
    voice_agg_clli: Optional[str] = Field(max_length=50)
    voice_agg_ip: Optional[str] = Field(max_length=3100)
    voice_agg_primary_port: Optional[str] = Field(max_length=4000)
    voice_agg_standby_port: Optional[str] = Field(max_length=4000)
    data_equipment_type: Optional[str] = Field(max_length=30)
    data_node_name: Optional[str] = Field(max_length=3100)
    data_node_up_slot: Optional[str] = Field(max_length=30)
    data_node_up_port: Optional[str] = Field(max_length=50)
    data_node_ip_address: Optional[str] = Field(max_length=3100)
    data_equipment_clli: Optional[str] = Field(max_length=50)
    data_slot: Optional[str] = Field(max_length=30)
    data_port: Optional[str] = Field(max_length=50)
    data_access_port_id: Optional[str] = Field(max_length=100)
    data_en: Optional[str] = Field(max_length=3100)
    data_el: Optional[str] = Field(max_length=3100)
    copper_cabinet: Optional[str] = Field(max_length=4000)
    cabinet_strip_pair_dp_pair: Optional[str] = Field(max_length=1)
    primary_strip_cable: Optional[str] = Field(max_length=80)
    secondary_strip_cable: Optional[str] = Field(max_length=80)
    data_v5_id: Optional[str] = Field(max_length=3100)
    data_exchange_id: Optional[str] = Field(max_length=3100)
    data_host_exchange_switch: Optional[str] = Field(max_length=3100)
    data_switch_id: Optional[str] = Field(max_length=3100)
    data_switch_type: Optional[str] = Field(max_length=3100)
    data_switch_name: Optional[str] = Field(max_length=3100)
    data_nms_jv_code: Optional[str] = Field(max_length=3100)
    data_agg_name: Optional[str] = Field(max_length=3100)
    data_agg_clli: Optional[str] = Field(max_length=50)
    data_agg_ip: Optional[str] = Field(max_length=3100)
    data_agg_primary_port: Optional[str] = Field(max_length=3100)
    data_agg_standby_port: Optional[str] = Field(max_length=3100)
    copper_plate_id: Optional[str] = Field(max_length=3100)
    plate_latitude: Optional[str] = Field(max_length=20)
    plate_id_longitude: Optional[str] = Field(max_length=20)
    domain_name: Optional[str] = None
    plate_district: Optional[str] = Field(max_length=3100)
    plate_region: Optional[str] = Field(max_length=3100)
    plate_exchange: Optional[str] = Field(max_length=3100)
    treatment_priority: Optional[str] = Field(max_length=1)
    mdf_name: Optional[str] = Field(max_length=100)
    mdf_slot: Optional[str] = Field(max_length=30)
    mdf_port: Optional[str] = Field(max_length=50)
    class_a: Optional[str] = Field(max_length=3100)
    telephone_number: Optional[str] = Field(max_length=3100)
    last_mod_ts: Optional[datetime] = None
    circuit_path_name: Optional[str] = Field(max_length=100) 
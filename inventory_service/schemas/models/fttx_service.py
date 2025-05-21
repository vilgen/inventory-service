from .base import SQLModel, Field, Optional, datetime

class InventoryFttxService(SQLModel, table=True):
    __tablename__ = "inventory_fttx_service"

    # Primary key field
    id: int = Field(default=None, primary_key=True)  # Auto-incrementing primary key

    service_id: Optional[str] = Field(max_length=100)
    service_type: Optional[str] = Field(max_length=30)
    service_status: Optional[str] = Field(max_length=20)
    tb_no: Optional[str] = Field(max_length=3100)
    tb_clli: Optional[str] = Field(max_length=3100)
    tb_lattitude: Optional[str] = Field(max_length=20)
    tb_longitude: Optional[str] = Field(max_length=20)
    tb_port: Optional[str] = Field(max_length=3100)
    tb_output_port: Optional[str] = Field(max_length=3100)
    tb_free_ports: Optional[str] = Field(max_length=4000)
    tb_utilized_ports: Optional[str] = Field(max_length=4000)
    fdt_no: Optional[str] = Field(max_length=4000)
    fdt_splitter_no: Optional[str] = Field(max_length=3100)
    fdt_clli: Optional[str] = Field(max_length=3100)
    fdt_splitter_output_port: Optional[str] = Field(max_length=3100)
    fdt_lattitude: Optional[str] = Field(max_length=3100)
    fdt_longitude: Optional[str] = Field(max_length=3100)
    olt_name: Optional[str] = Field(max_length=3100)
    olt_model: Optional[str] = Field(max_length=30)
    olt_slot: Optional[str] = Field(max_length=3100)
    olt_uplink_port: Optional[str] = Field(max_length=100)
    olt_pon_port: Optional[str] = Field(max_length=3100)
    olt_ip: Optional[str] = Field(max_length=3100)
    olt_aggregator: Optional[str] = Field(max_length=3100)
    olt_aggregator_ip: Optional[str] = Field(max_length=3100)
    olt_aggregator_primary_port: Optional[str] = Field(max_length=4000)
    olt_aggregator_standby_port: Optional[str] = Field(max_length=4000)
    olt_district: Optional[str] = Field(max_length=3100)
    olt_region: Optional[str] = Field(max_length=3100)
    olt_vendor: Optional[str] = Field(max_length=40)
    olt_up_port: Optional[str] = Field(max_length=50)
    olt_site: Optional[str] = Field(max_length=100)
    odf_id: Optional[str] = Field(max_length=4000)
    odf_input_port: Optional[str] = Field(max_length=4000)
    odf_output_port: Optional[str] = Field(max_length=4000)
    ont_serial_number: Optional[str] = Field(max_length=30)
    ont_model: Optional[str] = Field(max_length=30)
    ont_last_modify_date: Optional[datetime] = None
    ont_id: Optional[str] = Field(max_length=3100)
    ont_district: Optional[str] = Field(max_length=3100)
    ont_region: Optional[str] = Field(max_length=3100)
    ont_downstream_bandwidth: Optional[str] = Field(max_length=3100)
    ont_upstream_bandwidth: Optional[str] = Field(max_length=3100)
    business_unit: Optional[str] = None
    ebu_circuit_id: Optional[str] = Field(max_length=200)
    telephone_number: Optional[str] = Field(max_length=255)
    circuit_path_name: Optional[str] = Field(max_length=100)
    last_mod_ts: Optional[datetime] = None 
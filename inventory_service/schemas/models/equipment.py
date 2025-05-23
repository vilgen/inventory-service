from .base import SQLModel, Field, Optional, datetime

class InventoryEquipment(SQLModel, table=True):
    __tablename__ = "inventory_equipment"

    # Primary key field
    equip_inst_id: Optional[int] = Field(default=None, primary_key=True)
    last_mod_ts: Optional[datetime] = None
    type: Optional[str] = Field(max_length=30)
    port_status: Optional[str] = Field(max_length=20)
    port_number: Optional[str] = Field(max_length=50)
    card_status: Optional[str] = Field(max_length=20)
    card_type: Optional[str] = Field(max_length=50)
    slot_no: Optional[str] = Field(max_length=30)
    site_clli: Optional[str] = Field(max_length=100)
    site_number: Optional[str] = Field(max_length=30)
    inband_ip: Optional[str] = Field(max_length=3100)
    last_modified_time: Optional[datetime] = None
    equipment_model: Optional[str] = Field(max_length=30)
    equipment_vendor: Optional[str] = Field(max_length=40)
    status: Optional[str] = Field(max_length=20)
    equipment_type: Optional[str] = Field(max_length=30)
    shelf_number: Optional[str] = Field(max_length=20)
    equipment_name: Optional[str] = Field(max_length=200)
    p_last_mod_ts: Optional[datetime] = None 
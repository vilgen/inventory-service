from .base import SQLModel, Field, Optional, datetime

class InventoryCrossConnection(SQLModel, table=True):
    __tablename__ = "inventory_cross_connection"

    # Primary key fields
    id: int = Field(default=None, primary_key=True)  # Auto-incrementing primary key
    
    # Existing fields
    a_site_equipment_name: Optional[str] = Field(max_length=3100)
    a_site_equipment_type: Optional[str] = Field(max_length=30)
    a_site_equipment_vendor: Optional[str] = Field(max_length=40)
    a_site_ctp_id: Optional[str] = Field(max_length=30)
    a_site_shelf: Optional[str] = Field(max_length=12)
    a_site_slot: Optional[str] = Field(max_length=30)
    a_site_port: Optional[str] = Field(max_length=50)
    z_site_equipment_name: Optional[str] = Field(max_length=3100)
    z_site_equipment_type: Optional[str] = Field(max_length=30)
    z_site_equipment_vendor: Optional[str] = Field(max_length=40)
    z_site_ctp_id: Optional[str] = Field(max_length=30)
    z_site_shelf: Optional[str] = Field(max_length=12)
    z_site_slot: Optional[str] = Field(max_length=30)
    z_site_port: Optional[str] = Field(max_length=50)
    last_mod_ts: Optional[datetime] = None
    type: Optional[str] = Field(max_length=30) 
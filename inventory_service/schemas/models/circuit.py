from .base import SQLModel, Field, Optional, datetime

class InventoryCircuit(SQLModel, table=True):
    __tablename__ = "inventory_circuit"

    name: str = Field(max_length=100, primary_key=True)
    revision: Optional[int] = None
    category: str = Field(max_length=30)
    status: Optional[str] = Field(max_length=20)
    topology: Optional[str] = Field(max_length=1)
    bandwidth: Optional[str] = Field(max_length=30)
    a_site: Optional[str] = Field(max_length=100)
    a_ne_type: Optional[str] = Field(max_length=30)
    a_node_name: Optional[str] = Field(max_length=3100)
    a_port_bandwidth: Optional[str] = Field(max_length=30)
    a_port_name: Optional[str] = Field(max_length=50)
    a_slot_number: Optional[str] = Field(max_length=30)
    a_shelf_number: Optional[str] = Field(max_length=12)
    z_site: Optional[str] = Field(max_length=100)
    z_ne_type: Optional[str] = Field(max_length=30)
    z_node_name: Optional[str] = Field(max_length=3100)
    z_port_bandwidth: Optional[str] = Field(max_length=30)
    z_port_name: Optional[str] = Field(max_length=50)
    z_slot_number: Optional[str] = Field(max_length=30)
    z_shelf_number: Optional[str] = Field(max_length=12)
    last_mod_ts: Optional[datetime] = None 
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class InventoryCircuitElement(SQLModel, table=True):
    """Model representing the inventory_circ_element table."""
    
    __tablename__ = "inventory_circuit_element"

    # Primary key fields
    circuit_id: str = Field(max_length=100, primary_key=True)
    sequence_id: str = Field(max_length=500, primary_key=True)

    # Other fields
    category: Optional[str] = Field(max_length=30, default=None)
    card_name: Optional[str] = Field(max_length=30, default=None)
    card_port: Optional[str] = Field(max_length=81, default=None)
    card_description: Optional[str] = Field(max_length=100, default=None)
    port_access: Optional[str] = Field(max_length=100, default=None)
    a_site: Optional[str] = Field(max_length=100, default=None)
    a_node_name: Optional[str] = Field(max_length=3100, default=None)
    a_ne_type: Optional[str] = Field(max_length=30, default=None)
    a_port_bandwidth: Optional[str] = Field(max_length=30, default=None)
    a_port_name: Optional[str] = Field(max_length=30, default=None)
    a_slot_number: Optional[str] = Field(max_length=30, default=None)
    a_shelf_number: Optional[str] = Field(max_length=12, default=None)
    z_site: Optional[str] = Field(max_length=100, default=None)
    z_node_name: Optional[str] = Field(max_length=3100, default=None)
    z_ne_type: Optional[str] = Field(max_length=30, default=None)
    z_port_bandwidth: Optional[str] = Field(max_length=30, default=None)
    z_port_name: Optional[str] = Field(max_length=30, default=None)
    z_slot_number: Optional[str] = Field(max_length=30, default=None)
    z_shelf_number: Optional[str] = Field(max_length=12, default=None)
    connectivity: Optional[str] = Field(max_length=30, default=None)
    circ_path_inst_id: Optional[int] = Field(default=None)
    element_inst_id: Optional[int] = Field(default=None)

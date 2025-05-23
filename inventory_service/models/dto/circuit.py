from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional


class Circuit(BaseModel):
    name: Optional[str] = Field(None, description="Name of the circuit")
    category: Optional[str] = Field(None, description="Circuit type/category (e.g. IP, DIA, etc.)")
    status: Optional[str] = Field(None, description="Status of the circuit (e.g. LIVE)")
    topology: Optional[str] = Field(None, description="Topology type (e.g. Point to Point)")
    bandwidth: Optional[str] = Field(None, description="Bandwidth description")

    aSite: Optional[str] = Field(None, description="A-side site name")
    aNEType: Optional[str] = Field(None, description="A-side NE (Network Element) type")
    aNodeName: Optional[str] = Field(None, description="A-side node name")
    aPortBandwith: Optional[str] = Field(None, description="A-side port bandwidth")
    aPortName: Optional[str] = Field(None, description="A-side port name")
    aSlotNumber: Optional[str] = Field(None, description="A-side slot number")
    aShelfNumber: Optional[str] = Field(None, description="A-side shelf number")

    zSite: Optional[str] = Field(None, description="Z-side site name")
    zNodeName: Optional[str] = Field(None, description="Z-side node name")
    zNEType: Optional[str] = Field(None, description="Z-side NE type")
    zPortBandwith: Optional[str] = Field(None, description="Z-side port bandwidth")
    zPortName: Optional[str] = Field(None, description="Z-side port name")
    zSlotNumber: Optional[str] = Field(None, description="Z-side slot number")
    zShelfNumber: Optional[str] = Field(None, description="Z-side shelf number")


class CircuitType(str, Enum):
    DIA = "DIA"
    DIAS = "DIAS"
    IP = "IP"
    IPMW = "IPMW"
    PLL = "PLL"
    DLL = "DLL"
    MDIA = "MDIA"
    CBLS = "CBLS"
    SIP = "SIP"
    DIAL = "DIAL"
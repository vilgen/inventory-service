from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional


class CircuitInfo(BaseModel):
    name: str = Field(..., description="Name of the circuit")
    category: str = Field(..., description="Circuit type/category (e.g. IP, DIA, etc.)")
    status: str = Field(..., description="Status of the circuit (e.g. LIVE)")
    topology: str = Field(..., description="Topology type (e.g. Point to Point)")
    bandwidth: str = Field(..., description="Bandwidth description")

    aSite: str = Field(..., description="A-side site name")
    aNEType: Optional[str] = Field(None, description="A-side NE (Network Element) type")
    aNodeName: Optional[str] = Field(None, description="A-side node name")
    aPortBandwith: str = Field(..., description="A-side port bandwidth")
    aPortName: str = Field(..., description="A-side port name")
    aSlotNumber: str = Field(..., description="A-side slot number")
    aShelfNumber: str = Field(..., description="A-side shelf number")

    zSite: str = Field(..., description="Z-side site name")
    zNodeName: Optional[str] = Field(None, description="Z-side node name")
    zNEType: Optional[str] = Field(None, description="Z-side NE type")
    zPortBandwith: str = Field(..., description="Z-side port bandwidth")
    zPortName: str = Field(..., description="Z-side port name")
    zSlotNumber: str = Field(..., description="Z-side slot number")
    zShelfNumber: str = Field(..., description="Z-side shelf number")
class CircuitInfoListResponse(BaseModel):
    items: List[CircuitInfo] = Field(..., description="List of circuit information items")

    class Config:
        schema_extra = {
            "example": {
                "items": [
                    {
                        "name": "BISH09-BISH09 IP165",
                        "category": "IP",
                        "status": "LIVE",
                        "topology": "Point to Point",
                        "bandwidth": "2MBPS_E2E",
                        "aSite": "BSHARR00",
                        "aNEType": "",
                        "aNodeName": "",
                        "aPortBandwith": "2MBPS_E2E",
                        "aPortName": "LP 16_16",
                        "aSlotNumber": "1",
                        "aShelfNumber": "1",
                        "zSite": "BISH 016:0003",
                        "zNodeName": "",
                        "zNEType": "",
                        "zPortBandwith": "COPPER",
                        "zPortName": "02",
                        "zSlotNumber": "1",
                        "zShelfNumber": "1"
                    }
                ]
            }
        }

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


from typing import List
from inventory_service.models.dto.circuit_info import CircuitInfo
from pydantic import Field, RootModel

class CircuitInfoListResponse(RootModel):
    root: List[CircuitInfo] = Field(..., description="List of circuit information items")

    class Config:
        schema_extra = {
            "example": 
                 [
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
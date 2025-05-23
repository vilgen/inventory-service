
from pydantic import Field, RootModel
from inventory_service.models.dto.circuit_element import CircuitElement


class CircuitElementListResponse(RootModel):
    root: list[CircuitElement] = Field(..., description="List of circuit element sequences")

    class Config:
        schema_extra = {
            "example":
                 [
                    {
                        "circuitId": "BISH09-BISH09 IP165",
                        "sequence": [
                            {
                                "sequenceId": "1",
                                "category": "DSLAM",
                                "cardName": "05",
                                "cardPort": "LP 16_16",
                                "cardDescription": "",
                                "portAccess": "",
                                "aSite": "BSHARR00",
                                "aNodeName": "",
                                "aNEType": "",
                                "aPortBandwith": "2MBPS_E2E",
                                "aPortName": "",
                                "aSlotNumber": "1",
                                "aShelfNumber": "1",
                                "zSite": "BSHARR00",
                                "zNodeName": "",
                                "zNEType": "",
                                "zPortBandwith": "",
                                "zPortName": "",
                                "zSlotNumber": "1",
                                "zShelfNumber": "1",
                                "connectivity": ""
                            }
                        ]
                    }
                ]
            }
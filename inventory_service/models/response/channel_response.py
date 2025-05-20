from inventory_service.models.dto.channel import Channel
from pydantic import RootModel, Field
from typing import List

class ChannelListResponse(RootModel):
    """Model representing a list of circuit responses."""
    root: List[Channel] = Field(default_factory=list, description="List of circuit items")

    class Config:
        schema_extra = {
            "example": [
                    {
                        "ringName": "JEC331-1",
                        "termination": "101-00-000/ZNJA143",
                        "PRN": "89110",
                        "NI": "0/160316",
                        "RN": "",
                        "projectId": "Optimization 20",
                        "circuitNo": "9913",
                        "requirementType": "E1",
                        "requiredCircuitsNo": "1",
                        "facilityId": "IDEN/101-00-000-IDEN/ZNJA143",
                        "facilityTimeSlot": "|8#IMST_AU4|1#IMST_AU4",
                        "circuitTimeSlot": "361:IMST_E1",
                        "circuitName": "IDEN/101-00-000_IDEN/ZNJA143_30N01",
                        "status": "Live",
                        "bandwidth": "IMST_E1",
                        "aSite": "101-00-000",
                        "aNodeName": "10100000-5MU",
                        "aShelfNumber": "1",
                        "aSlotName": "SLOT TS8",
                        "aPortName": "PORT 36",
                        "aDdfOdfInfo": "00.302.06/02/10/36",
                        "zSite": "ZNJA143",
                        "zNodeName": "ZNJA143-DXX",
                        "zShelfNumber": "1",
                        "zSlotName": "ZNJA143_TN2",
                        "zPortName": "1.2.2.1",
                        "zDdfOdfInfo": "00.302.06/02/10/36",
                        "beneficiaryName": "-",
                        "PEAggName": "-",
                        "PEAggSlot": "-",
                        "PEAggPort": "-",
                        "PEAggBayloc": "-",
                        "protectionType": "None"
                    }
                ]
            }
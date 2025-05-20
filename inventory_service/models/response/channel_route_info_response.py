from inventory_service.models.dto.channel_route_info import ChannelRouteInfo
from pydantic import RootModel, Field
from typing import List
class ChannelRouteInfoListResponse(RootModel):
    """
    Model representing a list of channel route information items.
    """
    root: List[ChannelRouteInfo] = Field(default_factory=list, description="List of channel route items")

    class Config:
        schema_extra = {
            "example": [
                {
                    "sequence": "1",
                    "aSiteEquipmentName": "PE-AggX16-Abua-704-1",
                    "aSiteEquipmentType": "ETHERNET AGGREGATOR",
                    "aSiteCTPId": "10GE",
                    "aShelfNumber": "1",
                        "aSiteSlot": "1",
                        "aSitePort": "GE1/1/0",
                        "aDdfOdfInfo": "00.302.06/02/10/36",
                        "zSiteEquipmentName": "70400000/02HJ",
                        "zSiteEquipmentType": "DWDM",
                        "zSiteCTPId": "ODU2",
                        "zShelfNumber": "1",
                        "zSiteSlot": "SLOT 04",
                        "zSitePort": "ADDIN1",
                        "zDdfOdfInfo": "00.302.06/02/10/36"
                    },
                    {
                        "sequence": "2",
                        "aSiteEquipmentName": "70400000/02HJ",
                        "aSiteEquipmentType": "DWDM",
                        "aSiteCTPId": "ODU2",
                        "aShelfNumber": "1",
                        "aSiteSlot": "SLOT 04",
                        "aSitePort": "ADDIN1",
                        "aDdfOdfInfo": "00.302.06/02/10/36",
                        "zSiteEquipmentName": "70800000/02HJ",
                        "zSiteEquipmentType": "DWDM",
                        "zSiteCTPId": "ODU2",
                        "zShelfNumber": "1",
                        "zSiteSlot": "SLOT 05",
                        "zSitePort": "ADDIN2",
                        "zDdfOdfInfo": "00.302.06/02/10/37"
                    }
                ]
            }

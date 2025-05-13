from pydantic import BaseModel, Field


class ChannelRouteInfo(BaseModel):
    """
    Model representing channel route information between equipment.
    """
    sequence: str = Field(..., description="Sequence number of the route")
    aSiteEquipmentName: str = Field(..., description="Name of the equipment at the A site")
    aSiteEquipmentType: str = Field(..., description="Type of equipment at the A site")
    aSiteCTPId: str = Field(..., description="CTP ID of the equipment at the A site")
    aShelfNumber: str = Field(..., description="Shelf number of the equipment at the A site")
    aSiteSlot: str = Field(..., description="Slot of the equipment at the A site")
    aSitePort: str = Field(..., description="Port of the equipment at the A site")
    aDdfOdfInfo: str = Field(..., description="DDF/ODF information at the A site")
    zSiteEquipmentName: str = Field(..., description="Name of the equipment at the Z site")
    zSiteEquipmentType: str = Field(..., description="Type of equipment at the Z site")
    zSiteCTPId: str = Field(..., description="CTP ID of the equipment at the Z site")
    zShelfNumber: str = Field(..., description="Shelf number of the equipment at the Z site")
    zSiteSlot: str = Field(..., description="Slot of the equipment at the Z site")
    zSitePort: str = Field(..., description="Port of the equipment at the Z site")
    zDdfOdfInfo: str = Field(..., description="DDF/ODF information at the Z site")

    class Config:
        schema_extra = {
            "example": {
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
            }
        }


class ChannelRouteInfoListResponse(BaseModel):
    """
    Model representing a list of channel route information items.
    """
    items: list[ChannelRouteInfo] = Field(default_factory=list, description="List of channel route items")

    class Config:
        schema_extra = {
            "example": {
                "items": [
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
        }

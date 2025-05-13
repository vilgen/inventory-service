from dataclasses import Field
from enum import Enum

from pydantic import BaseModel, Field


class CrossConnectionType(str, Enum):
    """
    Enum representing different types of cross connections between network equipment.
    """
    # IMST System Cross Connections
    RAN_TRANSPORT_PE = "RAN_TRANSPORT_PE"
    OLT_TRANSPORT_PE = "OLT_TRANSPORT_PE"
    MSAN_TRANSPORT_PE = "MSAN_TRANSPORT_PE"
    PE_TRANSPORT_PE = "PE_TRANSPORT_PE"

    # RMS System Cross Connections
    RAN_MDU_OLT_PE = "RAN_MDU_OLT_PE"
    MDU_OLT = "MDU_OLT"
    OLT_PE = "OLT_PE"
    PE_PE = "PE_PE"


class CrossConnectionResponse(BaseModel):
    aSiteEquipmentName: str = Field(..., description="Name of the equipment at the A site")
    aSiteEquipmentType: str = Field(..., description="Type of equipment at the A site")
    aSiteEquipmentVendor: str = Field(..., description="Vendor of the equipment at the A site")
    aSiteCTPId: str = Field(..., description="CTP ID of the equipment at the A site")
    aSiteShelf: str = Field(..., description="Shell of the equipment at the A site")
    aSiteSlot: str = Field(..., description="Slot of the equipment at the A site")
    aSitePort: str = Field(..., description="Port of the equipment at the A site")
    zSiteEquipmentVendor: str = Field(..., description="Vendor of the equipment at the Z site")
    zSiteEquipmentName: str = Field(..., description="Name of the equipment at the Z site")
    zSiteEquipmentType: str = Field(..., description="Type of equipment at the Z site")
    zSiteCTPId: str = Field(..., description="CTP ID of the equipment at the Z site")
    zSiteShelf: str = Field(..., description="Shell of the equipment at the Z site")
    zSiteSlot: str = Field(..., description="Slot of the equipment at the Z site")
    zSitePort: str = Field(..., description="Port of the equipment at the Z site")
    class Config:
        schema_extra = {
            "example": {
                "aSiteEquipmentName": "PE-AggX16-Abua-704-1",
                "aSiteEquipmentType": "ETHERNET AGGREGATOR",
                "aSiteEquipmentVendor": "HUAWEI",
                "aSiteCTPId": "10GE",
                "aSiteShelf": "1",
                "aSiteSlot": "1",
                "aSitePort": "GE1/1/0",
                "zSiteEquipmentName": "70400000/02HJ",
                "zSiteEquipmentType": "DWDM",
                "zSiteEquipmentVendor": "HUAWEI",
                "zSiteCTPId": "ODU2",
                "zSiteShelf": "1",
                "zSiteSlot": "SLOT 04",
                "zSitePort": "ADDIN1"
            }
        }


class CrossConnectionListResponse(BaseModel):

    items: list[CrossConnectionResponse] = Field(default_factory=list, description="List of equipment items")
    class Config:
        schema_extra = {
            "example": {
                "items": [
                    {
                        "aSiteEquipmentName": "PE-AggX16-Abua-704-1",
                        "aSiteEquipmentType": "ETHERNET AGGREGATOR",
                        "aSiteEquipmentVendor": "HUAWEI",
                        "aSiteCTPId": "10GE",
                        "aSiteShelf": "1",
                        "aSiteSlot": "1",
                        "aSitePort": "GE1/1/0",
                        "zSiteEquipmentName": "70400000/02HJ",
                        "zSiteEquipmentType": "DWDM",
                        "zSiteEquipmentVendor": "HUAWEI",
                        "zSiteCTPId": "ODU2",
                        "zSiteShelf": "1",
                        "zSiteSlot": "SLOT 04",
                        "zSitePort": "ADDIN1"
                    },
                    {
                        "aSiteEquipmentName": "OLT-Site-333-1",
                        "aSiteEquipmentType": "OLT",
                        "aSiteEquipmentVendor": "HUAWEI",
                        "aSiteCTPId": "10GE",
                        "aSiteShelf": "1",
                        "aSiteSlot": "3",
                        "aSitePort": "GE1/0/6",
                        "zSiteEquipmentName": "PE-Router-708-1",
                        "zSiteEquipmentType": "PE ROUTER",
                        "zSiteEquipmentVendor": "HUAWEI",
                        "zSiteCTPId": "ODU2",
                        "zSiteShelf": "1",
                        "zSiteSlot": "SLOT 06",
                        "zSitePort": "GE2/0/6"
                    }
                ]
            }
        }

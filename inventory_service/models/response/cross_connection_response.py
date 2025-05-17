from pydantic import RootModel, Field
from typing import List
from inventory_service.models.dto.cross_connection import CrossConnection

class CrossConnectionListResponse(RootModel):
    root: List[CrossConnection] = Field(default_factory=list, description="List of equipment items")
    class Config:
        schema_extra = {
            "example":
              [
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

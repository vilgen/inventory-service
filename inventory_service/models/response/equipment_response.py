from inventory_service.models.dto.equipment import Equipment
from pydantic import RootModel, Field

class EquipmentListResponse(RootModel):

    root: list[Equipment] = Field(default_factory=list, description="List of equipment items")

    class Config:
        schema_extra = {
            "example": 
                [
                    {
                        "equipmentName": "108-00-310-MSAN MATB 1",
                        "shelfNumber": "1",
                        "equipmentType": "MSAN",
                        "equipmentStatus": "INSTALLED",
                        "equipmentVendor": "HUAWEI",
                        "equipmentModel": "UA5000",
                        "lastModifiedTime": "18-APR-2023",
                        "inBandIP": "10.11.10.1",
                        "siteNumber": "101-00-000",
                        "siteCLLI": "MURBRD00",
                        "slots": [
                            {
                                "slotNo": "02",
                                "cardType": "IPMB",
                                "cardStatus": "ASSIGNED",
                                "ports": [{"portNumber": "00", "portStatus": "Available"}]
                            }
                        ]
                    }
                ]
        }

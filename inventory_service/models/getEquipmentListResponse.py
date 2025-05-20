from enum import Enum

from pydantic import BaseModel, Field


class EquipmentType(str, Enum):
    DWDM = "DWDM"
    OTN = "OTN"
    SDH = "SDH"
    OPTICAL = "OPTICAL"

    # Fiber Access Equipment
    OLT = "OLT"
    FTTM_MDU = "FTTM-MDU"
    FTTH_OLT = "FTTH-OLT"
    FTTH_ONT = "FTTH-ONT"

    # Access Equipment
    UPE = "UPE"
    MBH = "MBH"
    ETHERNET_ACCESS = "ETHERNET ACCESS"
    DSLAM = "DSLAM"
    DSLAM_AGG = "DSLAM AGG"
    ETHERNET_AGGREGATOR = "ETHERNET AGGREGATOR"
    MSAN = "MSAN"

    # Switching Equipment
    SWITCH = "SWITCH"
    IP_SWITCH = "IP SWITCH"

    # Routing Equipment
    PE = "PE"
    PE_ROUTER = "PE ROUTER"

    # Radio Access Network Equipment
    RAN = "RAN"

    # Microwave Equipment
    MW = "MW"
    MW_LINK = "MW LINK"
    MW_NODE = "MW NODE"


class Port(BaseModel):
    portNumber: str = Field(..., description="Port number identifier")
    portStatus: str = Field(..., description="Current status of the port")

    class Config:
        schema_extra = {
            "example": {
                "portNumber": "1",
                "portStatus": "UP"
            }
        }

class PortCreate(Port):
    class Config:
        schema_extra = {
            "example": {
                "portNumber": "1",
                "portStatus": "UP"
            }
        }

class PortRead(Port):
    id: int = Field(..., description="Unique database ID for the port")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "portNumber": "1",
                "portStatus": "UP"
            }
        }
class Slot(BaseModel):
    slotNo: str = Field(..., description="Slot number identifier")
    cardType: str = Field(..., descriptions="Type of card installed")
    cardStatus: str = Field(..., description="Current status of the card")
    ports: list[Port] = Field(default_factory=list, description="List of ports on the card")

    class Config:
     schema_extra = {
        "example": {
            "slotNo": "1",
            "cardType": "MSAN",
            "cardStatus": "OK",
            "ports": [
                {
                    "portNumber": "1",
                    "portStatus": "UP"
                }
            ]
        }
    }
class Equipment(BaseModel):
    equipmentName: str = Field(..., description="Name of the equipment")
    shelfNumber: str = Field(..., description="Shelf number where equipment is installed")
    equipmentType: str = Field(..., description="Type of equipment")
    equipmentStatus: str = Field(..., description="Current status of the equipment")
    equipmentVendor: str = Field(..., description="Equipment vendor/manufacturer")
    equipmentModel: str = Field(..., description="Equipment model number")
    lastModifiedTime: str = Field(..., description="Last time the equipment was modified")
    inBandIP: str = Field(..., description="In-band IP address")
    siteNumber: str = Field(..., description="Site number identifier")
    siteCLLI: str = Field(..., description="Site CLLI code")
    slots: list[Slot] = Field(default_factory=list, description="List of slots in this equipment")
    class Config:
        schema_extra = {
            "example": {
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
        }

class EquipmentListResponse(BaseModel):

    items: list[Equipment] = Field(default_factory=list, description="List of equipment items")

    class Config:
        schema_extra = {
            "example": {
                "items": [
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
        }

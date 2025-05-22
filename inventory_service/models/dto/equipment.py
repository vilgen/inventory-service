from pydantic import BaseModel, Field
from enum import Enum
from typing import Dict, List

# Define the mappings at module level
GRANITE_MAPPINGS: Dict[str, List[str]] = {
    "DWDM": ["DWDM", "OTN"],
    "SDH": ["SDH", "OPTICAL"],
    "OLT": ["FTTM-MDU", "FTTH-OLT", "FTTH-ONT"],
    "UPE": ["MBH", "ETHERNET ACCESS"],
    "DSLAM": ["DSLAM"],
    "AGG": ["ETHERNET AGGREGATOR"],
    "MSAN": ["MSAN"],
    "SWITCH": ["IP SWITCH"],
    "PE": ["PE ROUTER"],
    "RAN": ["RAN"],
    "MW": ["MW LINK", "MW NODE"]
}

class EquipmentType(str, Enum):
    """
    Enum representing telecommunications equipment types with mapping between
    Autin categorization system and Granite categorization system.
    """
    # Define simple string values for str inheritance
    DWDM = "DWDM"
    SDH = "SDH"
    OLT = "OLT"
    UPE = "UPE"
    DSLAM = "DSLAM"
    AGG = "AGG"
    MSAN = "MSAN"
    SWITCH = "SWITCH"
    PE = "PE"
    RAN = "RAN"
    MW = "MW"
    
    @property
    def autin_name(self) -> str:
        """Return the Autin name."""
        return self.value
    
    @property
    def granite_names(self) -> List[str]:
        """Return the corresponding Granite equipment type names."""
        # Access the module-level mapping
        return GRANITE_MAPPINGS[self.value]
    
    @classmethod
    def from_string(cls, value: str) -> 'EquipmentType':
        """Look up an enum member by its Autin name."""
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"'{value}' is not a valid {cls.__name__}")


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

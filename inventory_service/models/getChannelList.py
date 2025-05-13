from enum import Enum

from pydantic import BaseModel, Field


class CircuitType(str, Enum):
    DWDM = "DWDM"
    SDH = "SDH"


class CircuitResponse(BaseModel):
    """Model representing a circuit response."""
    ringName: str = Field(..., description="Name of the ring")
    termination: str = Field(..., description="Termination point")
    PRN: str = Field(..., description="PRN identifier")
    NI: str = Field(..., description="Network identifier")
    RN: str = Field("", description="RN identifier")
    projectId: str = Field(..., description="Project identifier")
    circuitNo: str = Field(..., description="Circuit number")
    requirementType: str = Field(..., description="Type of requirement")
    requiredCircuitsNo: str = Field(..., description="Number of required circuits")
    facilityId: str = Field(..., description="Facility identifier")
    facilityTimeSlot: str = Field(..., description="Facility time slot")
    circuitTimeSlot: str = Field(..., description="Circuit time slot")
    circuitName: str = Field(..., description="Name of the circuit")
    status: str = Field(..., description="Status of the circuit")
    bandwidth: str = Field(..., description="Bandwidth of the circuit")
    aSite: str = Field(..., description="A site identifier")
    aNodeName: str = Field(..., description="A node name")
    aShelfNumber: str = Field(..., description="A shelf number")
    aSlotName: str = Field(..., description="A slot name")
    aPortName: str = Field(..., description="A port name")
    aDdfOdfInfo: str = Field(..., description="A DDF/ODF information")
    zSite: str = Field(..., description="Z site identifier")
    zNodeName: str = Field(..., description="Z node name")
    zShelfNumber: str = Field(..., description="Z shelf number")
    zSlotName: str = Field(..., description="Z slot name")
    zPortName: str = Field(..., description="Z port name")
    zDdfOdfInfo: str = Field(..., description="Z DDF/ODF information")
    beneficiaryName: str = Field("-", description="Name of the beneficiary")
    PEAggName: str = Field("-", description="PE aggregator name")
    PEAggSlot: str = Field("-", description="PE aggregator slot")
    PEAggPort: str = Field("-", description="PE aggregator port")
    PEAggBayloc: str = Field("-", description="PE aggregator bay location")
    protectionType: str = Field("None", description="Type of protection")

    class Config:
        schema_extra = {
            "example": {
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
        }


class CircuitListResponse(BaseModel):
    """Model representing a list of circuit responses."""
    items: list[CircuitResponse] = Field(default_factory=list, description="List of circuit items")

    class Config:
        schema_extra = {
            "example": {
                "items": [
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
        }

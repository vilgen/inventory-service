from pydantic import BaseModel, Field
from typing import List, Optional


class CircuitElementSequence(BaseModel):
    sequenceId: str = Field(..., description="Sequence ID")
    category: str = Field(..., description="Element category (e.g., DSLAM, CPU NTU)")
    cardName: str = Field(..., description="Card name")
    cardPort: str = Field(..., description="Card port")
    cardDescription: Optional[str] = Field(None, description="Card description")
    portAccess: Optional[str] = Field(None, description="Port access")

    aSite: str = Field(..., description="A-side site")
    aNodeName: Optional[str] = Field(None, description="A-side node name")
    aNEType: Optional[str] = Field(None, description="A-side NE type")
    aPortBandwith: Optional[str] = Field(None, description="A-side port bandwidth")
    aPortName: Optional[str] = Field(None, description="A-side port name")
    aSlotNumber: str = Field(..., description="A-side slot number")
    aShelfNumber: str = Field(..., description="A-side shelf number")

    zSite: str = Field(..., description="Z-side site")
    zNodeName: Optional[str] = Field(None, description="Z-side node name")
    zNEType: Optional[str] = Field(None, description="Z-side NE type")
    zPortBandwith: Optional[str] = Field(None, description="Z-side port bandwidth")
    zPortName: Optional[str] = Field(None, description="Z-side port name")
    zSlotNumber: str = Field(..., description="Z-side slot number")
    zShelfNumber: str = Field(..., description="Z-side shelf number")

    connectivity: Optional[str] = Field(None, description="Connectivity info")

class CircuitElement(BaseModel):
    circuitId: str = Field(..., description="Circuit ID")
    sequence: List[CircuitElementSequence] = Field(..., description="Sequence list of circuit elements")
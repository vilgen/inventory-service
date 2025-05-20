from enum import Enum
from pydantic import BaseModel, Field
from typing import List


class RingType(str, Enum):
    DWDM = "DWDM"
    SDH = "SDH"
class RingRouteInfo(BaseModel):
    aSite: str = Field(..., description="A-side site name")
    aNode: str = Field(..., description="A-side node name")
    aShelfNumber: str = Field(..., description="A-side shelf number")
    aSlot: str = Field(..., description="A-side slot")
    aPort: str = Field(..., description="A-side port")
    aDdfOdfInfo: str = Field(..., description="A-side DDF/ODF info")

    zSite: str = Field(..., description="Z-side site name")
    zNode: str = Field(..., description="Z-side node name")
    zShelfNumber: str = Field(..., description="Z-side shelf number")
    zSlot: str = Field(..., description="Z-side slot")
    zPort: str = Field(..., description="Z-side port")
    zDdfOdfInfo: str = Field(..., description="Z-side DDF/ODF info")

class RingInfo(BaseModel):
    RingName: str = Field(..., description="Name of the ring")
    termination: str = Field(..., description="Termination info")
    RingStatus: str = Field(..., description="Status of the ring")
    RingBandwidth: str = Field(..., description="Bandwidth of the ring")
    RingType: str = Field(..., description="Type of the ring (e.g., DWDM or SDH)")
    routeList: List[RingRouteInfo] = Field(..., description="List of route segments in the ring")


class RingInfoListResponse(BaseModel):
    items: List[RingInfo] = Field(..., description="List of ring information")

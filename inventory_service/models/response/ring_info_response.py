from typing import List

from inventory_service.models.dto.ring_info import RingInfo
from pydantic import Field, RootModel


class RingInfoListResponse(RootModel):
    root: List[RingInfo] = Field(..., description="List of ring information")
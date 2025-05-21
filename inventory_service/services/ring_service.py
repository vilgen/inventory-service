from datetime import datetime
from uuid import UUID
from typing import List

from inventory_service.models.dto.ring_info import RingInfo, RingRouteInfo


class RingService:
    async def get_rings(
        self,
        ring_type: str,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> List[RingInfo]:
        route_1 = RingRouteInfo(
            aSite="SITE-A1",
            aNode="NODE-A1",
            aShelfNumber="1",
            aSlot="SLOT-01",
            aPort="PORT-01",
            aDdfOdfInfo="00.302.06/02/10/36",
            zSite="SITE-Z1",
            zNode="NODE-Z1",
            zShelfNumber="1",
            zSlot="SLOT-02",
            zPort="PORT-02",
            zDdfOdfInfo="00.302.06/02/10/37"
        )

        route_2 = RingRouteInfo(
            aSite="SITE-A2",
            aNode="NODE-A2",
            aShelfNumber="1",
            aSlot="SLOT-03",
            aPort="PORT-03",
            aDdfOdfInfo="00.302.06/02/10/38",
            zSite="SITE-Z2",
            zNode="NODE-Z2",
            zShelfNumber="1",
            zSlot="SLOT-04",
            zPort="PORT-04",
            zDdfOdfInfo="00.302.06/02/10/39"
        )

        return [
            RingInfo(
                RingName="RING-123",
                termination="SITE-Z1",
                RingStatus="LIVE",
                RingBandwidth="10G",
                RingType=ring_type,
                routeList=[route_1, route_2]
            )
        ]
from datetime import datetime
from uuid import UUID

from ..models.channelRouteInfo import ChannelRouteInfo


class ChannelRouteService:
    """
    Service for channel route-related operations.
    """

    async def get_channel_route_info(
        self,
        prn: str,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> list[ChannelRouteInfo]:
        """
        Fetch channel route information based on PRN and time range.
        
        Args:
            prn: Project Reference Number
            start_time: Start time for filtering
            end_time: End time for filtering
            client_msg_ref: Client message reference
            correlation_ref: Correlation reference
            
        Returns:
            List of channel route information
        """

        # Mock implementation - in a real scenario, you would fetch data from a database or another service
        # based on the PRN and time range
        mock_route_1 = ChannelRouteInfo(
            sequence="1",
            aSiteEquipmentName="PE-AggX16-Abua-704-1",
            aSiteEquipmentType="ETHERNET AGGREGATOR",
            aSiteCTPId="10GE",
            aShelfNumber="1",
            aSiteSlot="1",
            aSitePort="GE1/1/0",
            aDdfOdfInfo="00.302.06/02/10/36",
            zSiteEquipmentName="70400000/02HJ",
            zSiteEquipmentType="DWDM",
            zSiteCTPId="ODU2",
            zShelfNumber="1",
            zSiteSlot="SLOT 04",
            zSitePort="ADDIN1",
            zDdfOdfInfo="00.302.06/02/10/36"
        )

        mock_route_2 = ChannelRouteInfo(
            sequence="2",
            aSiteEquipmentName="70400000/02HJ",
            aSiteEquipmentType="DWDM",
            aSiteCTPId="ODU2",
            aShelfNumber="1",
            aSiteSlot="SLOT 04",
            aSitePort="ADDIN1",
            aDdfOdfInfo="00.302.06/02/10/36",
            zSiteEquipmentName="70800000/02HJ",
            zSiteEquipmentType="DWDM",
            zSiteCTPId="ODU2",
            zShelfNumber="1",
            zSiteSlot="SLOT 05",
            zSitePort="ADDIN2",
            zDdfOdfInfo="00.302.06/02/10/37"
        )

        # You could add logic here to filter or customize the mock data based on the PRN
        # For example, if the PRN matches a certain pattern, return different routes

        return [mock_route_1, mock_route_2]

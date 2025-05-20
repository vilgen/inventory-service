from datetime import datetime
from uuid import UUID

from inventory_service.models.dto.channel import Channel, ChannelType
from inventory_service.models.response.channel_response import ChannelListResponse

class ChannelService:
    """
    Service for channel-related operations.
    """

    async def get_channel_list(
        self,
        channel_type: ChannelType,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> list[Channel]:
        """
        Fetch channel list based on type, status, and time range.
        
        Args:
            channel_type: Type of channel to retrieve
            status: Optional status to filter by
            start_time: Start time for filtering
            end_time: End time for filtering
            client_msg_ref: Client message reference
            correlation_ref: Correlation reference
            
        Returns:
            List of channel responses
        """
        # Mock implementation
        mock_channel1 = Channel(
            ringName="JEC331-1",
            termination="101-00-000/ZNJA143",
            PRN="89110",
            NI="0/160316",
            RN="",
            projectId="Optimization 20",
            circuitNo="9913",
            requirementType=channel_type.value,
            requiredCircuitsNo="1",
            facilityId="IDEN/101-00-000-IDEN/ZNJA143",
            facilityTimeSlot="|8#IMST_AU4|1#IMST_AU4",
            circuitTimeSlot="361:IMST_E1",
            circuitName="IDEN/101-00-000_IDEN/ZNJA143_30N01",
            status= "Live",
            bandwidth=f"IMST_{channel_type.value}",
            aSite="101-00-000",
            aNodeName="10100000-5MU",
            aShelfNumber="1",
            aSlotName="SLOT TS8",
            aPortName="PORT 36",
            aDdfOdfInfo="00.302.06/02/10/36",
            zSite="ZNJA143",
            zNodeName="ZNJA143-DXX",
            zShelfNumber="1",
            zSlotName="ZNJA143_TN2",
            zPortName="1.2.2.1",
            zDdfOdfInfo="00.302.06/02/10/36",
        )

        mock_channel2 = Channel(
            ringName="JEC331-2",
            termination="101-00-000/ZNJA144",
            PRN="89111",
            NI="0/160317",
            RN="",
            projectId="Optimization 20",
            circuitNo="9914",
            requirementType=channel_type.value,
            requiredCircuitsNo="1",
            facilityId="IDEN/101-00-000-IDEN/ZNJA144",
            facilityTimeSlot="|9#IMST_AU4|2#IMST_AU4",
            circuitTimeSlot="362:IMST_E1",
            circuitName="IDEN/101-00-000_IDEN/ZNJA144_30N02",
            status="Live",
            bandwidth=f"IMST_{channel_type.value}",
            aSite="101-00-000",
            aNodeName="10100000-5MU",
            aShelfNumber="1",
            aSlotName="SLOT TS9",
            aPortName="PORT 37",
            aDdfOdfInfo="00.302.06/02/10/37",
            zSite="ZNJA144",
            zNodeName="ZNJA144-DXX",
            zShelfNumber="1",
            zSlotName="ZNJA144_TN2",
            zPortName="1.2.2.2",
            zDdfOdfInfo="00.302.06/02/10/37",
        )

        return ChannelListResponse(root=[mock_channel1, mock_channel2])

    async def get_channel_by_id(
        self,
        channel_id: str,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> Channel:
        """
        Fetch a specific channel by ID.
        
        Args:
            channel_id: ID of the channel to retrieve
            client_msg_ref: Client message reference
            correlation_ref: Correlation reference
            
        Returns:
            Channel response
        """
        # Mock implementation
        mock_channel = Channel(
            ringName="JEC331-1",
            termination="101-00-000/ZNJA143",
            PRN="89110",
            NI="0/160316",
            RN="",
            projectId="Optimization 20",
            circuitNo=channel_id,
            requirementType="E1",
            requiredCircuitsNo="1",
            facilityId="IDEN/101-00-000-IDEN/ZNJA143",
            facilityTimeSlot="|8#IMST_AU4|1#IMST_AU4",
            circuitTimeSlot="361:IMST_E1",
            circuitName="IDEN/101-00-000_IDEN/ZNJA143_30N01",
            status="Live",
            bandwidth="IMST_E1",
            aSite="101-00-000",
            aNodeName="10100000-5MU",
            aShelfNumber="1",
            aSlotName="SLOT TS8",
            aPortName="PORT 36",
            aDdfOdfInfo="00.302.06/02/10/36",
            zSite="ZNJA143",
            zNodeName="ZNJA143-DXX",
            zShelfNumber="1",
            zSlotName="ZNJA143_TN2",
            zPortName="1.2.2.1",
            zDdfOdfInfo="00.302.06/02/10/36",
        )

        return ChannelListResponse(root=[mock_channel])

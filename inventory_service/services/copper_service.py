from datetime import datetime
from uuid import UUID
from inventory_service.config.database import get_session
from inventory_service.models.response.copper_response import CopperListResponse
from inventory_service.models.dto.copper import Copper
from inventory_service.schemas.models.copper_service import InventoryCopperService
from inventory_service.services.base_service import BaseService
from fastapi import Depends
from inventory_service.utils.mapper import Mapper
from sqlmodel import Session


class CopperService(BaseService[InventoryCopperService]):
    """
    Service for copper route-related operations.
    """
    def __init__(self, session: Session = Depends(get_session)):
        super().__init__(InventoryCopperService, session)

    async def get_by_last_mod_ts(
        self,
        start_datetime: datetime,
        end_datetime: datetime
    ) -> CopperListResponse:
        """Get copper services by last modification timestamp range and convert to CopperListResponse."""
        copper_services = await self.get_by_datetime_range(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            timestamp_field="last_mod_ts"
        )
        
        # Map each copper service to Copper using the Mapper
        copper_routes = [Mapper.map_to_copper_service_info(service) for service in copper_services]
        
        # Create and return the response
        return CopperListResponse(root=copper_routes)
    
    async def get_copper_routes(
        self,
        route_type: str,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> list[Copper]:
        """
        Fetch copper route information based on route type and time range.

        Args:
            route_type: Type of copper route (e.g., "COPPER_LINK")
            start_time: Start time for filtering
            end_time: End time for filtering
            client_msg_ref: Client message reference UUID
            correlation_ref: Correlation reference UUID

        Returns:
            List of copper route information
        """

        # Mock implementation - replace with real DB/service call as needed
        mock_route = Copper(
            pathname="MNAREAAT-FSLY 076:0146-COPPER_LINK 5116307",
            category="COPPER_LINK",
            voiceEquipmentType="MSAN",
            voiceExchangeID="MNAREAAT-MSAN FSY9A/00001-0",
            voiceEquipmentCLLI="Area PP#699/1 (E076)",
            voiceSlot="06",
            voicePort="19",
            voiceAccessPortID="MNAREAAT-MSAN FSY9A/00001-0",
            voiceEN="N0000100019",
            voiceNodeName="M302-32-306_AFSY9",
            voiceNodeUpSlot="",
            voiceNodeUpPort="",
            voiceNodeIPAddress="",
            voiceV5ID="",
            voiceSwitchID="FSY9A",
            voiceHostExchangeSwitch="FSY11",
            voiceSwitchType="NGN Huawei MSAN",
            voiceSwitchName="NGN PRINCE MOHD__302-32-306",
            voiceNMSJVCode="",
            voiceSwitchModel="",
            voiceAggName="",
            voiceAggCLLI="",
            voiceAggIP="",
            voiceAggPrimaryPort="",
            voiceAggStandbyPort="",
            dataEquipmentType="MDF",
            dataNodeName="FSY9A-001",
            dataNodeUpSlot="",
            dataNodeUpPort="",
            dataNodeIPAddress="",
            dataEquipmentCLLI="MNAREAAT",
            dataSlot="001",
            dataPort="015",
            dataAccessPortID="",
            dataEN="",
            dataEL="",
            copperCabinet=["P-1-10", "S-145-154"],
            cabinetStripPairDPPair="",
            primaryStripCable="FSY9A E01-00002",
            secondaryStripCable="FSLY 076:0146",
            dataV5ID="",
            dataExchangeID="",
            dataHostExchangeSwitch="",
            dataSwitchID="",
            dataSwitchType="",
            dataSwitchName="",
            dataNMSJVCode="",
            dataAggName="",
            dataAggCLLI="",
            dataAggIP="",
            dataAggPrimaryPort="",
            dataAggStandbyPort="",
            copperPlateID="FSLY 076:0146",
            plateLatitude="",
            plateIDLongitude="",
            domainName="hbu__domain",
            plateDistrict="",
            plateRegion="",
            plateExchange="",
            treatmentPriority="",
            MDFName="",
            MDFSlot="",
            MDFPort="",
            classA="",
            telephoneNumber="138110554"
        )

        return CopperListResponse(root=[mock_route])

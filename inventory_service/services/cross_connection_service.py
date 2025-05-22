from datetime import datetime
from uuid import UUID

from inventory_service.config.database import get_session
from inventory_service.models.dto.cross_connection import CrossConnection, CrossConnectionType
from inventory_service.models.response.cross_connection_response import CrossConnectionListResponse
from inventory_service.services.base_service import BaseService
from fastapi import Depends
from inventory_service.utils.mapper import Mapper
from sqlmodel import Session
from inventory_service.schemas.models.cross_connection import InventoryCrossConnection

class CrossConnectionService(BaseService[InventoryCrossConnection]):
    """
    Service for cross-connection related operations.
    """
    def __init__(self, session: Session = Depends(get_session)):
        super().__init__(InventoryCrossConnection, session)

    async def get_by_last_mod_ts_and_type(
        self,
        start_datetime: datetime,
        end_datetime: datetime,
        type: CrossConnectionType = CrossConnectionType.OLT_PE
    ) -> CrossConnectionListResponse:
        """
        Get cross connections by last modified timestamp.
        """
        cross_connections = await self.get_by_datetime_range_and_type(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            type=type,
            type_field="type"
        )
        cross_connections = [Mapper.map_to_cross_connection(cross_connection) for cross_connection in cross_connections]
        return CrossConnectionListResponse(root=cross_connections)

    async def get_cross_connections(
        self,
        connection_type: CrossConnectionType,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> list[CrossConnection]:
        """
        Fetch cross connections based on type and time range.
        """
        # Return mock data - just one example as requested
        mock_cross_connection = CrossConnection(
                aSiteEquipmentName="PE-AggX16-Abua-704-1",
                aSiteEquipmentType="ETHERNET AGGREGATOR",
                aSiteEquipmentVendor="HUAWEI",
                aSiteCTPId="10GE",
                aSiteShelf="1",
                aSiteSlot="1",
                aSitePort="GE1/1/0",
                zSiteEquipmentName="70400000/02HJ",
                zSiteEquipmentType="DWDM",
                zSiteEquipmentVendor="HUAWEI",
                zSiteCTPId="ODU2",
            zSiteShelf="1",
            zSiteSlot="SLOT 04",
            zSitePort="ADDIN1"
        )
        return CrossConnectionListResponse(root=[mock_cross_connection])

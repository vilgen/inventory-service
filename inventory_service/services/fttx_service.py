from datetime import datetime
from typing import List, Optional
from uuid import UUID
from sqlmodel import Session
from fastapi import Depends

from inventory_service.models.dto.fttx import FTTHLinkInfo
from inventory_service.models.response.fttx_response import FTTHLinkInfoListResponse
from inventory_service.schemas.models.fttx_service import InventoryFttxService
from inventory_service.services.base_service import BaseService
from inventory_service.utils.mapper import Mapper
from ..config.database import get_session

class FttxService(BaseService[InventoryFttxService]):
    """Service class for FTTX inventory operations."""
    
    def __init__(self, session: Session = Depends(get_session)):
        super().__init__(InventoryFttxService, session)

    async def get_by_last_mod_ts(
        self,
        start_datetime: datetime,
        end_datetime: datetime
    ) -> FTTHLinkInfoListResponse:
        """Get FTTX services by last modification timestamp range and convert to FTTHLinkInfoListResponse."""
        fttx_services = await self.get_by_datetime_range(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            timestamp_field="last_mod_ts"
        )
        
        # Map each FTTX service to FTTHLinkInfo using the Mapper
        ftth_links = [Mapper.map_to_ftth_link_info(service) for service in fttx_services]
        
        # Create and return the response
        return FTTHLinkInfoListResponse(root=ftth_links)

    async def get_fttx_service_info(
        self,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> FTTHLinkInfoListResponse:
        """
        Fetch FTTX service information based on time range.
        
        Args:
            start_time: Start time for filtering
            end_time: End time for filtering
            client_msg_ref: Client message reference
            correlation_ref: Correlation reference
            
        Returns:
            List of FTTX service information
        """
       
        
        # Mock implementation - in a real scenario, you would fetch data from a database or another service
        mock_ftth_link_1 = FTTHLinkInfo(
            serviceID="MRSTRD01-NZHARDU1568-1-FTTH_LINK 001",
            serviceType="FTTH_LINK",
            serviceStatus="LIVE",
            TBNo="NZHARDU1568",
            TBCLLI="NZHARDU1568",
            TBLattitude="24.7529548",
            TBLongitude="46.6991209",
            TBPort="BUILTIN-01",
            TBOutputPort="01",
            TBFreePorts=["28", "31"],
            TBUtilizedPorts=["01", "02", "03"],
            FDTNo="NZHARDU1568-1",
            FDTSPlitterNo="ESUL F121-1-6",
            FDTCLLI="NZHARDJ1173",
            FDTSPlitterOutputPort="ESUL F121-6-18-6-18",
            FDTLattitude="24.7519",
            FDTLongitude="46.7028",
            OLTName="116-00_MRSTRD00OLG",
            OLTModel="MA5680T",
            OLTSLot="01",
            OLTUplinkPort="2",
            OLTPONPort="1",
            OLTIP="10.72.96.131",
            OLTAggregator="PE-AggX16A-Wadi-789-31-2",
            OLTAggregatorIP="192.168.111.202",
            OLTAggregatorPrimaryPort="0-4",
            OLTAggregatorStandbyPort="0-6",
            OLTDistrict="",
            OLTRegion="",
            OLTVendor="",
            OLTUpPort="",
            OLTSite="SABDRR02",
            ODFID="00/02.03/07",
            ODFInputPort="15RX",
            ODFOutputPort="16TX",
            ONTSerialNumber="485754431FB29D11",
            ONTModel="HG8245",
            ONTLastModifyDate="",
            ONTID="MRSTRD00OLG",
            ONTDistrict="",
            ONTRegion="",
            ONTDownStreamBandwidth="",
            ONTUpStreamBandwidth="",
            businessUnit="hbu__domain",
            circuitPathName="MRSTRD01-NZHARDU1568-1-FTTH_LINK 001",
            EBUCircuitID="BISH09-BISH09 IP165",
            telephoneNumber="114554101"
        )
        
        mock_ftth_link_2 = FTTHLinkInfo(
            serviceID="MRSTRD02-NZHARDU1569-1-FTTH_LINK 002",
            serviceType="FTTH_LINK",
            serviceStatus="PENDING",
            TBNo="NZHARDU1569",
            TBCLLI="NZHARDU1569",
            TBLattitude="24.7581234",
            TBLongitude="46.7054321",
            TBPort="BUILTIN-02",
            TBOutputPort="02",
            TBFreePorts=["05", "12", "18"],
            TBUtilizedPorts=["01", "03", "04"],
            FDTNo="NZHARDU1569-1",
            FDTSPlitterNo="ESUL F121-2-4",
            FDTCLLI="NZHARDJ1174",
            FDTSPlitterOutputPort="ESUL F121-4-20-4-20",
            FDTLattitude="24.7575",
            FDTLongitude="46.7070",
            OLTName="116-01_MRSTRD01OLG",
            OLTModel="MA5670T",
            OLTSLot="02",
            OLTUplinkPort="3",
            OLTPONPort="2",
            OLTIP="10.72.96.132",
            OLTAggregator="PE-AggX16A-Wadi-789-31-3",
            OLTAggregatorIP="192.168.111.203",
            OLTAggregatorPrimaryPort="0-5",
            OLTAggregatorStandbyPort="0-7",
            OLTDistrict="DistrictA",
            OLTRegion="Region1",
            OLTVendor="VendorX",
            OLTUpPort="UP1",
            OLTSite="SABDRR03",
            ODFID="00/02.03/08",
            ODFInputPort="17RX",
            ODFOutputPort="18TX",
            ONTSerialNumber="485754432FB29D12",
            ONTModel="HG8247",
            ONTLastModifyDate="2025-05-10T14:32:00Z",
            ONTID="MRSTRD01OLG",
            ONTDistrict="DistrictB",
            ONTRegion="Region2",
            ONTDownStreamBandwidth="100Mbps",
            ONTUpStreamBandwidth="20Mbps",
            businessUnit="hbu__residential",
            circuitPathName="MRSTRD02-NZHARDU1569-1-FTTH_LINK 002",
            EBUCircuitID="BISH10-BISH10 IP166",
            telephoneNumber="114554102"
        )
        
        # Apply filters based on time range
        # In real implementation, you'd apply the start_time and end_time filters to database query
        # For now, we just return the mock data
        return FTTHLinkInfoListResponse(root=[mock_ftth_link_1, mock_ftth_link_2])
        
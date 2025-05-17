
from fastapi import APIRouter, Depends, Path

from inventory_service.models.response.channel_route_info_response import ChannelRouteInfoListResponse
from inventory_service.models.response.fttx_response import FTTHLinkInfoListResponse
from inventory_service.models.response.equipment_response import EquipmentListResponse
from inventory_service.models.response.channel_response import ChannelListResponse
from inventory_service.models.response.cross_connection_response import CrossConnectionListResponse
from inventory_service.models.dto.channel import ChannelType
from inventory_service.models.dto.cross_connection import CrossConnectionType
from inventory_service.models.dto.equipment import EquipmentType


from inventory_service.services.channel_route_info_service import ChannelRouteService
from inventory_service.services.channel_service import ChannelService
from inventory_service.services.cross_connection_service import CrossConnectionService
from inventory_service.services.fttx_service import FTTXService
from inventory_service.services.equipment_service import EquipmentService

from ..middleware.header_validation import validate_service_id
from ..middleware.time_range_validator import TimeRangeParams



router = APIRouter(
    prefix="/api/v1/granite",
    tags=["Equipment"],
)

@router.get(
    "/crossConnection/{cross_connection_type}",
    response_model=CrossConnectionListResponse,
    summary="Get Cross Connection List",
    description="Retrieves a list of cross connections."
)
async def get_cross_connection_list(
    cross_connection_type: CrossConnectionType = Path(
        ...,
        description="Type of cross connection to retrieve"
    ),
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getCrossConnectionList")),
    cross_connection_service: CrossConnectionService = Depends(),
):
    return await cross_connection_service.get_cross_connections(
        connection_type=cross_connection_type,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )


@router.get(
    "/equipment/{equipment_type}",
    response_model=EquipmentListResponse,
    summary="Get Equipment List",
    description="Retrieves a list of equipment filtered by type and time range."
)
async def get_equipment_list(
    equipment_type: EquipmentType = Path(
        ...,
        description="Type of equipment to retrieve"
    ),
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getEquipmentList")),
    equipment_service: EquipmentService = Depends(),
):
    """
    Retrieve a list of equipment based on type and time range.
    """
    return await equipment_service.get_equipment_list(
        equipment_type=equipment_type,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )

@router.get(
    "/channel/{channel_type}",
    response_model=ChannelListResponse,
    summary="Get Channel List",
    description="Retrieves a list of channels filtered by type, status, and time range."
)
async def get_channel_list(
    channel_type: ChannelType = Path(
        ...,
        description="Type of channel to retrieve"
    ),
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getChannelList")),
    channel_service: ChannelService = Depends(),
):
    """
    Retrieve a list of channels based on type, status, and time range.
    """
    return await channel_service.get_channel_list(
        channel_type=channel_type,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )


@router.get(
    "/channelRoute/{prn}",
    response_model=ChannelRouteInfoListResponse,
    summary="Get Channel Route Information",
    description="Retrieves channel route information for a specific PRN (Project Reference Number)."
)
async def get_channel_route_info(
    prn: str = Path(
        ...,
        description="Project Reference Number (PRN) to retrieve channel route information for"
    ),
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getChannelRouteInfo")),
    channel_route_service: ChannelRouteService = Depends(),
):
    """
    Retrieve channel route information for a specific PRN.
    """
    return await channel_route_service.get_channel_route_info(
        prn=prn,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )

@router.get(
    "/fttxService",
    response_model=FTTHLinkInfoListResponse,
    summary="Get FTTX Service Information",
    description="Retrieves FTTX service information within the specified time range."
)
async def get_fttx_service(
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getFTTXService")),
    fttx_service: FTTXService = Depends(),
):
    """
    Retrieve FTTX service information within the specified time range.
    """
    return await fttx_service.get_fttx_service_info(
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )
    
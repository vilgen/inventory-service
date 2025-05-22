from fastapi import APIRouter, Depends, Path
from typing import List, Optional
from datetime import datetime

# DTOs
from inventory_service.models.dto.channel import ChannelType
from inventory_service.models.dto.circuit_info import CircuitType
from inventory_service.models.dto.cross_connection import CrossConnectionType
from inventory_service.models.dto.equipment import EquipmentType
from inventory_service.models.dto.ring_info import RingType

# Response Models
from inventory_service.models.response.channel_response import ChannelListResponse
from inventory_service.models.response.channel_route_info_response import ChannelRouteInfoListResponse
from inventory_service.models.response.circuit_element_response import CircuitElementListResponse
from inventory_service.models.response.circuit_info_response import CircuitInfoListResponse
from inventory_service.models.response.copper_route_response import CopperRouteInfoListResponse
from inventory_service.models.response.cross_connection_response import CrossConnectionListResponse
from inventory_service.models.response.equipment_response import EquipmentListResponse
from inventory_service.models.response.fttx_response import FTTHLinkInfoListResponse
from inventory_service.models.response.ring_info_response import RingInfoListResponse

# Services
from inventory_service.services.channel_route_info_service import ChannelRouteService
from inventory_service.services.channel_service import ChannelService
from inventory_service.services.circuit_element_service import CircuitElementService
from inventory_service.services.circuit_service import CircuitService
from inventory_service.services.copper_service import CopperRouteService
from inventory_service.services.cross_connection_service import CrossConnectionService
from inventory_service.services.equipment_service import EquipmentService
from inventory_service.services.fttx_service import FttxService
from inventory_service.services.ring_service import RingService

# Utils
from inventory_service.utils.validation import TimeRangeParams, validate_service_id

router = APIRouter(
    prefix="/api/v1/granite",
    tags=["Inventory Services"],
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
    equipment_type: EquipmentType,
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getEquipmentList")),
    equipment_service: EquipmentService = Depends()
):
    """Get equipment list filtered by type and time range."""
    return await equipment_service.get_equipment_by_type(
        equipment_type=equipment_type,
        start_time=time_params.start_time,
        end_time=time_params.end_time
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
    fttx_service: FttxService = Depends(),
):
    """
    Retrieve FTTX service information within the specified time range.
    """
    return await fttx_service.get_by_last_mod_ts(
        start_datetime=time_params.start_time,
        end_datetime=time_params.end_time,
    )
    

@router.get(
    "/copper/{copper_route_type}",
    response_model=CopperRouteInfoListResponse,
    summary="Get Copper Route List",
    description="Retrieves a list of copper route connections."
)
async def get_copper_route_list(
    copper_route_type: str = Path(
        ..., description="Type of copper route to retrieve"
    ),
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getCopperRouteList")),
    copper_route_service: CopperRouteService = Depends(),
):
    routes = await copper_route_service.get_copper_routes(
        route_type=copper_route_type,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )
    return  routes
@router.get(
    "/circuit/{circuitType}",
    response_model=CircuitInfoListResponse,
    summary="Get Circuit Data",
    description="Returns created or updated circuit data for the given circuit type between startTime and endTime."
)
async def get_circuit_data(
    circuitType: CircuitType = Path(..., description="Type of circuit to retrieve"),
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getCircuitData")),
    circuit_service: CircuitService = Depends(),
):
    circuits = await circuit_service.get_circuits(
        circuit_type=circuitType.value,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )
    return circuits

@router.get(
    "/circuitElement",
    response_model=CircuitElementListResponse,
    summary="Get Circuit Element List",
    description="Returns circuit element sequences for the given circuit ID within a time range."
)
async def get_circuit_element_list(
    circuitId: str = Path(..., description="Circuit name returned from circuit list response"),
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getCircuitElementList")),
    circuit_element_service: CircuitElementService = Depends(),
):
    data = await circuit_element_service.get_circuit_elements(
        circuit_id=circuitId,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )
    return data

@router.get(
    "/ring",
    response_model=RingInfoListResponse,
    summary="Get Ring List",
    description="Retrieves rings of a specific type created or updated between the given dates."
)
async def get_ring_list(
    ringType: RingType = Path(..., description="Type of ring (DWDM or SDH)"),
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getRingList")),
    ring_service: RingService = Depends(),
):
    rings = await ring_service.get_rings(
        ring_type=ringType.value,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )
    return rings
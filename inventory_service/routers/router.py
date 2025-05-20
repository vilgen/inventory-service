
from fastapi import APIRouter, Depends, Path

from inventory_service.models.RingInfoListResponse import RingInfoListResponse, RingType
from inventory_service.models.channelRouteInfo import ChannelRouteInfoListResponse
from inventory_service.models.circuitElement import CircuitElementListResponse
from inventory_service.models.circuitInfo import CircuitInfoListResponse, CircuitType
from inventory_service.models.copperRouteInfo import CopperRouteInfoListResponse
from inventory_service.models.fttxList import FTTHLinkInfoListResponse
from inventory_service.models.getChannelList import ChannelListResponse,ChannelResponse,ChannelType
from inventory_service.models.getCrossConnectionResponse import (
    CrossConnectionListResponse,
    CrossConnectionType,
)
from inventory_service.services import RingService
from inventory_service.services.channelRouteInfoService import ChannelRouteService
from inventory_service.services.channelService import CircuitService
from inventory_service.services.crossConnectionService import CrossConnectionService
from inventory_service.services.fttxService import FTTXService

from ..middleware.header_validation import validate_service_id
from ..middleware.time_range_validator import TimeRangeParams
from ..models.getEquipmentListResponse import Equipment, EquipmentType
from ..services.equipmentService import EquipmentService
from inventory_service.services.copperService import CopperRouteService
router = APIRouter(
    prefix="/api/v1/granite",
    tags=["Equipment"],
)
@router.get(
    "/cross-connection/{cross_connection_type}",
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
    connections = await cross_connection_service.get_cross_connections(
        connection_type=cross_connection_type,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )

    return {"items": connections}


@router.get(
    "/equipment/{equipment_type}",
    response_model=list[Equipment],
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
    equipment_list = await equipment_service.get_equipment_list(
        equipment_type=equipment_type,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )

    return equipment_list

@router.get(
    "/circuits/{channel_type}",
    response_model=ChannelListResponse,
    summary="Get Circuit List",
    description="Retrieves a list of circuits filtered by type, status, and time range."
)
async def get_channel_list(
    channel_type: ChannelType = Path(
        ...,
        description="Type of circuit to retrieve"
    ),
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getCircuitList")),
    circuit_service: CircuitService = Depends(),
):
    """
    Retrieve a list of circuits based on type, status, and time range.
    """
    circuit_list = await circuit_service.get_channel_list(
        circuit_type=channel_type,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )

    return {"items": circuit_list}

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
    route_info_list = await channel_route_service.get_channel_route_info(
        prn=prn,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )

    return {"items": route_info_list}
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
    fttx_links = await fttx_service.get_fttx_service_info(
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )
    
    return {"items": fttx_links}

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
    return {"items": routes}
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
    return {"items": circuits}

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
    return {"items": data}

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
    return {"items": rings}
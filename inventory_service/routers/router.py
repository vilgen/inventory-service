
from fastapi import APIRouter, Depends, Path
from inventory_service.models.getChannelList import CircuitListResponse, CircuitType
from inventory_service.models.getCrossConnectionResponse import CrossConnectionListResponse, CrossConnectionResponse, CrossConnectionType
from inventory_service.services.circuitService import CircuitService
from inventory_service.services.crossConnectionService import CrossConnectionService

from ..middleware.header_validation import validate_service_id
from ..models.getEquipmentListResponse import Equipment, EquipmentType
from ..services.equipmentService import EquipmentService
from ..middleware.time_range_validator import TimeRangeParams

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
    "/circuits/{circuit_type}",
    response_model=CircuitListResponse,
    summary="Get Circuit List",
    description="Retrieves a list of circuits filtered by type, status, and time range."
)
async def get_circuit_list(
    circuit_type: CircuitType = Path(
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
    circuit_list = await circuit_service.get_circuit_list(
        circuit_type=circuit_type,
        start_time=time_params.start_time,
        end_time=time_params.end_time,
        client_msg_ref=headers["client_msg_ref"],
        correlation_ref=headers["correlation_ref"]
    )

    return {"items": circuit_list}
from fastapi import APIRouter, Depends, Path, Query
from typing import List, Optional
from datetime import datetime

# DTOs
from inventory_service.models.dto.circuit import CircuitType
from inventory_service.models.dto.cross_connection import CrossConnectionType
from inventory_service.models.dto.equipment import EquipmentType

# Response Models

from inventory_service.models.response.circuit_element_response import CircuitElementListResponse
from inventory_service.models.response.circuit_response import CircuitListResponse
from inventory_service.models.response.copper_response import CopperListResponse
from inventory_service.models.response.cross_connection_response import CrossConnectionListResponse
from inventory_service.models.response.equipment_response import EquipmentListResponse
from inventory_service.models.response.fttx_response import FTTHLinkInfoListResponse

# Services
from inventory_service.services import (
    CrossConnectionService, CopperService, 
    FttxService, CircuitElementService, CircuitService, 
    EquipmentService)

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
    return await cross_connection_service.get_by_last_mod_ts_and_type(
        start_datetime=time_params.start_time,
        end_datetime=time_params.end_time,
        type=cross_connection_type
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
    "/fttxService",
    response_model=FTTHLinkInfoListResponse,
    summary="Get FTTX Service Information",
    description="Retrieves FTTX service information within the specified time range."
)
async def get_fttx_service_list(
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getFTTXList")),
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
    "/copperService",
    response_model=CopperListResponse,
    summary="Get Copper Service List",
    description="Retrieves a list of copper services."
)
async def get_copper_service_list(
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getCopperList")),
    copper_service: CopperService = Depends(),
):
    return await copper_service.get_by_last_mod_ts(
        start_datetime=time_params.start_time,
        end_datetime=time_params.end_time,
    )

@router.get(
    "/circuit/{circuitType}",
    response_model=CircuitListResponse,
    summary="Get Circuit List",
    description="Returns created or updated circuit data for the given circuit type between startTime and endTime."
)
async def get_circuit_list(
    circuitType: CircuitType = Path(..., description="Type of circuit to retrieve"),
    time_params: TimeRangeParams = Depends(),
    headers: dict = Depends(validate_service_id("getCircuitList")),
    circuit_service: CircuitService = Depends(),
):
    return await circuit_service.get_by_last_mod_ts_and_type(
        start_datetime=time_params.start_time,
        end_datetime=time_params.end_time,
        type=circuitType
    )

@router.get(
    "/circuitElement",
    response_model=CircuitElementListResponse,
    summary="Get Circuit Element List",
    description="Returns circuit element sequences for the given circuit ID."
)
async def get_circuit_element_list(
    circuitId: str = Query(..., description="Circuit ID to fetch elements for"),
    headers: dict = Depends(validate_service_id("getCircuitElementList")),
    circuit_element_service: CircuitElementService = Depends(),
):
    return await circuit_element_service.get_by_circuit_id(
        circuit_id=circuitId,
    )

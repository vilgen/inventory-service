from datetime import datetime
from uuid import UUID
from typing import List

from inventory_service.models.dto.circuit import Circuit, CircuitType
from inventory_service.models.response.circuit_response import CircuitListResponse
from inventory_service.services.base_service import BaseService
from fastapi import Depends
from inventory_service.utils.mapper import Mapper
from sqlmodel import Session
from inventory_service.schemas.models.circuit import InventoryCircuit
from inventory_service.config.database import get_session

class CircuitService(BaseService[InventoryCircuit]):
    """
    Service for retrieving circuit data.
    """
    def __init__(self, session: Session = Depends(get_session)):
        super().__init__(InventoryCircuit, session)

    async def get_by_last_mod_ts_and_type(
        self,
        start_datetime: datetime,
        end_datetime: datetime,
        type: CircuitType
    ) -> CircuitListResponse:
        circuits = await self.get_by_datetime_range_and_type(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            type=type,
            type_field="category"
        )
        circuits = [Mapper.map_to_circuit(circuit) for circuit in circuits]
        return CircuitListResponse(root=circuits)
        
    async def get_circuits(
        self,
        circuit_type: str,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> List[Circuit]:
        """
        Fetch circuit data filtered by circuit type and time range.

        Args:
            circuit_type: Type of circuit (e.g., IP, DIA, etc.)
            start_time: Start time in ISO8601 format
            end_time: End time in ISO8601 format
            client_msg_ref: UUID from headers for traceability
            correlation_ref: UUID for correlation tracking

        Returns:
            List of CircuitInfo objects
        """

        # Mock data - In real usage, fetch from DB or external system
        mock_circuit = Circuit(
            name="BISH09-BISH09 IP165",
            category=circuit_type,
            status="LIVE",
            topology="Point to Point",
            bandwidth="2MBPS_E2E",
            aSite="BSHARR00",
            aNEType="",
            aNodeName="",
            aPortBandwith="2MBPS_E2E",
            aPortName="LP 16_16",
            aSlotNumber="1",
            aShelfNumber="1",
            zSite="BISH 016:0003",
            zNodeName="",
            zNEType="",
            zPortBandwith="COPPER",
            zPortName="02",
            zSlotNumber="1",
            zShelfNumber="1"
        )

        return CircuitListResponse(root=[mock_circuit])

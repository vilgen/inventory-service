from datetime import datetime
from typing import List
from uuid import UUID
from inventory_service.models.dto.circuit_element import CircuitElement, CircuitElementSequence
from inventory_service.models.response.circuit_element_response import CircuitElementListResponse
from inventory_service.services.base_service import BaseService
from fastapi import Depends
from inventory_service.config.database import get_session
from inventory_service.utils.mapper import Mapper
from sqlmodel import Session, select
from inventory_service.schemas.models.circuit_element import InventoryCircuitElement

class CircuitElementService(BaseService[InventoryCircuitElement]):
    """
    Service for retrieving circuit element sequence data.
    """
    def __init__(self, session: Session = Depends(get_session)):
        super().__init__(InventoryCircuitElement, session)

    async def get_by_circuit_id(
        self,
        circuit_id: str
    ) -> CircuitElementListResponse:
        """Get circuit elements by circuit ID."""
        circuit_elements = await self.get_by_id_str(
            id=circuit_id,
            id_field="circuit_id"
        )
        # Map to DTOs
        mapped_elements = [Mapper.map_to_circuit_element(elem) for elem in circuit_elements]
        print(f"Mapped elements: {mapped_elements}")
        
        # Group by circuit_id and create sequence list
        circuit_element_map = {}
        for elem in mapped_elements:
            if elem.circuitId not in circuit_element_map:
                circuit_element_map[elem.circuitId] = []
            circuit_element_map[elem.circuitId].append(elem.sequence[0])  # Each element has one sequence
        
        # Create final response
        response_elements = [
            CircuitElement(
                circuitId=circuit_id,
                sequence=sequences
            )
            for circuit_id, sequences in circuit_element_map.items()
        ]
        
        return CircuitElementListResponse(root=response_elements)
    
    async def get_circuit_elements(
        self,
        circuit_id: str,
        start_time: datetime,
        end_time: datetime,
        client_msg_ref: UUID,
        correlation_ref: UUID
    ) -> List[CircuitElement]:
        """
        Fetch circuit element data for the given circuit ID and time range.

        Args:
            circuit_id: Name of the circuit (from getCircuitList response)
            start_time: Start time for filtering (ISO8601)
            end_time: End time for filtering (ISO8601)
            client_msg_ref: UUID from request headers
            correlation_ref: UUID from request headers

        Returns:
            List of CircuitElement objects with sequence details
        """

        # Mock data
        mock_sequence_1 = CircuitElementSequence(
            sequenceId="1",
            category="DSLAM",
            cardName="05",
            cardPort="LP 16_16",
            cardDescription="",
            portAccess="",
            aSite="BSHARR00",
            aNodeName="",
            aNEType="",
            aPortBandwith="2MBPS_E2E",
            aPortName="",
            aSlotNumber="1",
            aShelfNumber="1",
            zSite="BSHARR00",
            zNodeName="",
            zNEType="",
            zPortBandwith="",
            zPortName="",
            zSlotNumber="1",
            zShelfNumber="1",
            connectivity=""
        )

        mock_sequence_2 = CircuitElementSequence(
            sequenceId="2",
            category="CPU NTU",
            cardName="1",
            cardPort="1",
            cardDescription="",
            portAccess="",
            aSite="BSHARR00",
            aNodeName="",
            aNEType="",
            aPortBandwith="",
            aPortName="",
            aSlotNumber="1",
            aShelfNumber="1",
            zSite="BSHARR00",
            zNodeName="",
            zNEType="",
            zPortBandwith="",
            zPortName="",
            zSlotNumber="1",
            zShelfNumber="1",
            connectivity=""
        )
        circuit_element_1 = CircuitElement(
                circuitId=circuit_id,
                sequence=[mock_sequence_1, mock_sequence_2]
            )            
        return CircuitElementListResponse(root=[circuit_element_1])
from datetime import datetime
from typing import Literal
from uuid import UUID

from fastapi import Depends, Header, HTTPException, status


async def validate_common_headers(
    client_msg_ref: UUID = Header(..., alias="X-STC-ESB-ClientMsgRef"),
    correlation_ref: UUID = Header(..., alias="X-STC-ESB-CorrelationRef"),
    timestamp: datetime = Header(..., alias="X-STC-ESB-Timestamp"),
    system_id: Literal["HIM"] = Header(..., alias="X-STC-ESB-SystemId"),
) -> dict:
    """Validate common headers required for all API endpoints."""
    return {
        "client_msg_ref": client_msg_ref,
        "correlation_ref": correlation_ref,
        "timestamp": timestamp,
        "system_id": system_id,
    }

def validate_service_id(expected_service_id: str):
    """Factory function to create service ID validators for specific endpoints."""
    async def validator(
        common_headers: dict = Depends(validate_common_headers),
        service_id: str = Header(..., alias="X-STC-ESB-ServiceId")
    ) -> dict:
        if service_id != expected_service_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid service ID. Expected '{expected_service_id}'."
            )

        # Add service_id to headers dict
        headers = {**common_headers, "service_id": service_id}
        return headers

    return validator

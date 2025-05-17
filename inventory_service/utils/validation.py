from datetime import datetime, timedelta
from typing import Literal, Dict, Optional, Callable
from uuid import UUID

from fastapi import Depends, Header, HTTPException, status, Request
from pydantic import BaseModel, validator

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

def validate_service_id(service_id: str) -> Callable:
    """
    Create a validator function for service ID that also stores headers in request state.
    """
    async def validate(
        request: Request,
        client_msg_ref: UUID = Header(..., alias="X-STC-ESB-ClientMsgRef"),
        correlation_ref: UUID = Header(..., alias="X-STC-ESB-CorrelationRef"),
        timestamp: datetime = Header(..., alias="X-STC-ESB-Timestamp"),
        system_id: Literal["HIM"] = Header(..., alias="X-STC-ESB-SystemId"),
        service_id_header: str = Header(..., alias="X-STC-ESB-ServiceId", pattern=f"^{service_id}$")
    ) -> Dict:
        # Store headers in request state for middleware
        request.state.headers = {
            "client_msg_ref": client_msg_ref,
            "correlation_ref": correlation_ref,
            "timestamp": timestamp,
            "system_id": system_id,
            "service_id": service_id_header
        }
        
        return {
            "client_msg_ref": client_msg_ref,
            "correlation_ref": correlation_ref,
            "timestamp": timestamp,
            "system_id": system_id,
            "service_id": service_id_header
        }
    
    return validate

class TimeRangeParams(BaseModel):
    start_time: datetime
    end_time: datetime
    
    @validator('end_time')
    def validate_time_range(cls, end_time, values):
        start_time = values.get('start_time')
        if start_time is None:
            return end_time
        if end_time - start_time > timedelta(days=2):
            raise ValueError("Time range must be less than 2 days")
        if start_time > end_time:
            raise ValueError("Start time must be before end time")
        return end_time




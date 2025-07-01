from datetime import datetime, timedelta
from typing import Literal, Dict, Optional, Callable
from uuid import UUID
from fastapi import Depends, Header, HTTPException, status, Request, Query
from pydantic import BaseModel, field_validator, model_validator, ValidationError

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
    
    @model_validator(mode='after')
    def validate_time_range(self):
        # Check if start time is before end time
        if self.start_time > self.end_time:
            raise ValueError("Start time must be before end time")
        
        # Check if time range is more than 2 days
        time_diff = self.end_time - self.start_time
        if time_diff > timedelta(days=2):
            raise ValueError(
                f"Time range must be less than 2 days. "
                f"Current range: {time_diff.days} days, {time_diff.seconds//3600} hours"
            )
        
        return self

# Create a dependency function that handles the validation and converts errors to HTTP 400
def get_time_range_params(
    start_time: datetime = Query(..., description="Start time for the query range"),
    end_time: datetime = Query(..., description="End time for the query range")
) -> TimeRangeParams:
    """
    Dependency function to validate time range parameters.
    This will convert Pydantic ValidationError to HTTP 400 instead of 500.
    """
    try:
        return TimeRangeParams(start_time=start_time, end_time=end_time)
    except ValidationError as e:
        # Extract the error message from Pydantic ValidationError
        error_details = []
        for error in e.errors():
            if error['type'] == 'value_error':
                error_details.append(error['msg'])
            else:
                error_details.append(f"{error['loc'][-1]}: {error['msg']}")
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "Invalid time range",
                "message": "; ".join(error_details),
                "code": "TIME_RANGE_VALIDATION_ERROR"
            }
        )
    except Exception as e:
        # Catch any other unexpected errors
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "Invalid time range",
                "message": str(e),
                "code": "TIME_RANGE_VALIDATION_ERROR"
            }
        )
# app/middleware/custom_headers.py
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from fastapi import FastAPI
from typing import Callable
from datetime import datetime

class AddCustomHeaderMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Get the response from the route handler
        response = await call_next(request)
        
        # Get headers from request state if they exist
        if hasattr(request.state, "headers"):
            headers = request.state.headers
            # Add custom headers to response
            if "client_msg_ref" in headers:
                response.headers["X-STC-ESB-ClientMsgRef"] = str(headers["client_msg_ref"])
            if "correlation_ref" in headers:
                response.headers["X-STC-ESB-CorrelationRef"] = str(headers["correlation_ref"])
            if "timestamp" in headers:
                response.headers["X-STC-ESB-Timestamp"] = datetime.now().isoformat()
            if "system_id" in headers:
                response.headers["X-STC-ESB-SystemId"] = "inventory-service"
            if "service_id" in headers:
                # Append "_Response" to the service ID
                response.headers["X-STC-ESB-ServiceId"] = f"{str(headers['service_id'])}_Response"
        
        return response

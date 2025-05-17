from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .middleware.custom_response_header import AddCustomHeaderMiddleware
from .routers.router import router

app = FastAPI(
    title="Inventory Service Data API",
    description="API for managing network inventory data",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add custom header middleware
app.add_middleware(AddCustomHeaderMiddleware)

# Include routers
app.include_router(router)
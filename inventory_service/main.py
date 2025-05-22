from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from inventory_service.config.database import create_db_and_tables, init_db
from inventory_service.middleware.custom_response_header import AddCustomHeaderMiddleware
from inventory_service.routers.router import router


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

@app.on_event("startup")
async def on_startup():
    # Create database tables
    create_db_and_tables()
    # Initialize database with data
    init_db()
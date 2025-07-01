from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from inventory_service.config.database import test_connection, check_database_health
from inventory_service.middleware.custom_response_header import AddCustomHeaderMiddleware
from inventory_service.routers.router import router
from inventory_service.routers.auth_router import auth_router

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


# Include routers
app.include_router(router)
app.include_router(auth_router)

@app.on_event("startup")
async def on_startup():
    """Startup tasks - only verify connection"""
    print("🚀 Starting Inventory Service...")
    
    # Test database connection
    if test_connection():
        print("✅ Database connection verified")
        
        # Optional: Check if tables exist
        try:
            health = check_database_health()
            print(f"📊 Database: {health['database']} | User: {health['user']}")
        except Exception as e:
            print(f"⚠️ Health check warning: {e}")
    else:
        print("❌ Database connection failed!")
        # Don't exit - let the app start anyway for debugging
    
    print("🎉 Startup complete!")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Inventory Service API is running",
        "version": "1.0.0",
        "status": "operational"
    }

@app.get("/health")
async def health_check():
    """Basic health check endpoint"""
    return {"status": "healthy", "service": "inventory-service"}

@app.get("/health/database")
async def database_health():
    """Detailed database health check"""
    return check_database_health()
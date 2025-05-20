from fastapi import FastAPI

from inventory_service.routers.portRouter import port_router
from inventory_service.routers.router import router
from inventory_service.utils.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(port_router)
app.include_router(router)
@app.get("/")
async def root():
    return {"message": "Hello World"}

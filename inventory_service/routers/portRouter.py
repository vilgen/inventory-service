from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.getEquipmentListResponse import PortCreate, PortRead
from ..services.portService import get_port, get_ports, create_port
from ..utils.deps import get_db

port_router = APIRouter(prefix="/ports", tags=["ports"])

@port_router.get("/", response_model=list[PortRead])
def read_ports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ports = get_ports(db, skip, limit)
    return ports

@port_router.get("/{port_id}", response_model=PortRead)
def read_port(port_id: int, db: Session = Depends(get_db)):
    db_port = get_port(db, port_id)
    if not db_port:
        raise HTTPException(status_code=404, detail="Port not found")
    return db_port

@port_router.post("/", response_model=PortRead, status_code=201)
def add_port(port_in: PortCreate, db: Session = Depends(get_db)):
    new_port = create_port(db, port_in)
    return new_port

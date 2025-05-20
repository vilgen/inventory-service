from sqlalchemy.orm import Session
from ..schemas.portORM import PortORM
from ..models.dto.equipment import Port


def get_port(db: Session, port_id: int) -> PortORM | None:
    return db.query(PortORM).filter(PortORM.id == port_id).first()


def get_ports(db: Session, skip: int = 0, limit: int = 100) -> list[PortORM]:
    return db.query(PortORM).offset(skip).limit(limit).all()


def create_port(db: Session, port_in: Port) -> PortORM:
    db_obj = PortORM(
        port_number=port_in.portNumber,
        port_status=port_in.portStatus
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
from sqlalchemy import Column, Integer, String
from ..utils.database import Base


class PortORM(Base):
    __tablename__ = "ports"

    id = Column(Integer, primary_key=True, index=True)
    port_number = Column(String, nullable=False, index=True)
    port_status = Column(String, nullable=False)

    @property
    def portNumber(self) -> str:
        return self.port_number

    @property
    def portStatus(self) -> str:
        return self.port_status
    
    
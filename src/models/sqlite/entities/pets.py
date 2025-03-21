from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class PetsTable(Base):
  __tablename__ = 'pets'

  id = Column(BIGINT, primary_key=True)
  name = Column(String, nullable=False)
  Type = Column(String, nullable=False)

  def __repr__(self) -> str:
    return f"Pets [name={self.name}, Type={self.Type}]"
  
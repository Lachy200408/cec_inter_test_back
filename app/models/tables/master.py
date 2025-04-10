from app.models.base.master import MasterBase
from sqlmodel import Field
from uuid import UUID, uuid4

class MasterEntity(MasterBase, table=True):
	__tablename__ = "masters"
	id: UUID = Field(default_factory=uuid4, primary_key=True)
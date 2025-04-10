from app.models.base.testimony import TestimonyBase
from sqlmodel import Field
from uuid import UUID, uuid4

class TestimonyEntity(TestimonyBase, table=True):
	__tablename__ = "testimonies"
	id: UUID = Field(default_factory=uuid4, primary_key=True)
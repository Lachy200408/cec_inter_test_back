from uuid import UUID, uuid4
from app.models.base.course import CourseBase
from sqlmodel import Field

class CourseEntity(CourseBase, table=True):
	__tablename__ = "courses"
	id: UUID = Field(default_factory=uuid4, primary_key=True)
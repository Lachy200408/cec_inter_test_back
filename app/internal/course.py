from app.models.request.course import CourseRequest
from app.models.response.course import CourseResponse
from app.models.tables.course import CourseEntity
from app.config.postgres import DBSession
from sqlmodel import select
from uuid import UUID

async def get_all(db: DBSession):
  try:
  	courses = db.exec(select(CourseEntity)).all()
  	return courses
  except Exception as e:
    raise e

async def get_by_id(db: DBSession, id: UUID):
  try:
  	course = db.exec(select(CourseEntity).where(CourseEntity.id == id)).first()
  	return course
  except Exception as e:
    raise e
  
async def get_popular(db: DBSession):
  try:
  	courses = db.exec(select(CourseEntity).where(CourseEntity.rating > 2).order_by(CourseEntity.rating.desc())).all()
  	return courses
  except Exception as e:
    raise e

async def create(db: DBSession, course: CourseRequest):
	try:
		new_course = CourseEntity(**course.dict())
		db.add(new_course)
		db.commit()
		db.refresh(new_course)
		return new_course
	except Exception as e:
		raise e
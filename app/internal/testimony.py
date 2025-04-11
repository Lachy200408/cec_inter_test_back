from app.models.request.testimony import TestimonyRequest
from app.models.response.testimony import TestimonyResponse
from app.models.tables.testimony import TestimonyEntity
from app.config.postgres import DBSession
from sqlmodel import select
from uuid import UUID

async def get_all(db: DBSession):
  try:
  	testimonies = db.exec(select(TestimonyEntity)).all()
  	return testimonies
  except Exception as e:
    raise e

async def get_by_id(db: DBSession, id: UUID):
  try:
  	testimony = db.exec(select(TestimonyEntity).where(TestimonyEntity.id == id)).first()
  	return testimony
  except Exception as e:
    raise e

async def create(db: DBSession, testimony: TestimonyRequest):
	try:
		new_testimony = TestimonyEntity(**testimony.dict())
		db.add(new_testimony)
		db.commit()
		db.refresh(new_testimony)
		return new_testimony
	except Exception as e:
		raise e

async def delete_all(db: DBSession):
  try:
    db.delete(TestimonyEntity)
    db.commit()
  except Exception as e:
    raise e
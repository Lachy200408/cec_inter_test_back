from app.models.request.master import MasterRequest
from app.models.response.master import MasterResponse
from app.models.tables.master import MasterEntity
from app.config.postgres import DBSession
from sqlmodel import select
from uuid import UUID

async def get_all(db: DBSession):
  try:
  	masters = db.exec(select(MasterEntity)).all()
  	return masters
  except Exception as e:
    raise e

async def get_by_id(db: DBSession, id: UUID):
  try:
  	master = db.exec(select(MasterEntity).where(MasterEntity.id == id)).first()
  	return master
  except Exception as e:
    raise e

async def create(db: DBSession, master: MasterRequest):
	try:
		new_master = MasterEntity(**master.dict())
		db.add(new_master)
		db.commit()
		db.refresh(new_master)
		return new_master
	except Exception as e:
		raise e
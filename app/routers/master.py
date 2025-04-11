from typing import Annotated, Union
from app.internal import master as master_service
from app.models.response.master import MasterResponse
from app.models.request.master import MasterRequest
from app.config.postgres import DBDependency
from fastapi import APIRouter, Body, Query

router = APIRouter(
	prefix="/masters",
  tags=["Masters"],
)

@router.get("/", response_model=list[MasterResponse])
async def get_all(db: DBDependency, q: Annotated[Union[int, None], Query()]=None):
  return (await master_service.get_all(db))[0:q]

@router.get("/{id}", response_model=MasterResponse)
async def get_by_id(id: str, db: DBDependency):
  return await master_service.get_by_id(db, id)

@router.post("/", response_model=MasterResponse)
async def create_master(master: Annotated[MasterRequest, Body()], db: DBDependency):
  return await master_service.create(db, master)

@router.delete("/")
async def delete_all(db: DBDependency):
  return await master_service.delete_all(db)
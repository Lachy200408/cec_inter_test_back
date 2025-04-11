from typing import Annotated, Union
from app.internal import testimony as testimony_service
from app.models.response.testimony import TestimonyResponse
from app.models.request.testimony import TestimonyRequest
from app.config.postgres import DBDependency
from fastapi import APIRouter, Body, Query

router = APIRouter(
	prefix="/testimonies",
  tags=["Testimonies"],
)

@router.get("/", response_model=list[TestimonyResponse])
async def get_all(db: DBDependency, q: Annotated[Union[int, None], Query()]=None):
  return (await testimony_service.get_all(db))[0:q]

@router.get("/{id}", response_model=TestimonyResponse)
async def get_by_id(id: str, db: DBDependency):
  return await testimony_service.get_by_id(db, id)

@router.post("/", response_model=TestimonyResponse)
async def create_testimony(testimony: Annotated[TestimonyRequest, Body()], db: DBDependency):
  return await testimony_service.create(db, testimony)

@router.delete("/")
async def delete_all(db: DBDependency):
  return await testimony_service.delete_all(db)
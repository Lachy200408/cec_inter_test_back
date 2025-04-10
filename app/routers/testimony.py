from typing import Annotated
from app.internal import testimony as testimony_service
from app.models.response.testimony import TestimonyResponse
from app.models.request.testimony import TestimonyRequest
from app.config.postgres import DBDependency
from fastapi import APIRouter, Body

router = APIRouter(
	prefix="/testimonies",
  tags=["Testimonies"],
)

@router.get("/", response_model=list[TestimonyResponse])
async def get_all_testimonies(db: DBDependency):
  return await testimony_service.get_all(db)

@router.get("/{id}", response_model=TestimonyResponse)
async def get_all_testimonies(id: str, db: DBDependency):
  return await testimony_service.get_by_id(db, id)

@router.post("/", response_model=TestimonyResponse)
async def create_testimony(testimony: Annotated[TestimonyRequest, Body()], db: DBDependency):
  return await testimony_service.create(db, testimony)
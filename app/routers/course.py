from typing import Annotated, Union
from app.internal import course as course_service
from app.models.response.course import CourseResponse
from app.models.request.course import CourseRequest
from app.models.base.course_category import CourseCategoryBase
from app.config.postgres import DBDependency
from fastapi import APIRouter, Body, Path, Query

router = APIRouter(
	prefix="/courses",
  tags=["Courses"],
)

@router.get("/", response_model=list[CourseResponse])
async def get_all(db: DBDependency, q: Annotated[Union[int, None], Query()]=None):
  return (await course_service.get_all(db))[0:q]

@router.get("/popular", response_model=list[CourseResponse])
async def get_popular(db: DBDependency, q: Annotated[Union[int, None], Query()]=None):
  return (await course_service.get_popular(db))[0:q]

@router.get("/category/{category}", response_model=list[CourseResponse])
async def get_by_category(
  category: CourseCategoryBase,
  db: DBDependency,
  q: Annotated[Union[int, None], Query()]=None
):
  return (await course_service.get_by_category(db, category))[0:q]

@router.get("/{id}", response_model=CourseResponse)
async def get_by_id(id: str, db: DBDependency):
  return await course_service.get_by_id(db, id)

@router.post("/", response_model=CourseResponse)
async def create_course(course: Annotated[CourseRequest, Body()], db: DBDependency):
  return await course_service.create(db, course)

@router.delete("/")
async def delete_all(db: DBDependency):
  return await course_service.delete_all(db)
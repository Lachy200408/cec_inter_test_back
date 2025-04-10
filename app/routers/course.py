from typing import Annotated
from app.internal import course as course_service
from app.models.response.course import CourseResponse
from app.models.request.course import CourseRequest
from app.config.postgres import DBDependency
from fastapi import APIRouter, Body

router = APIRouter(
	prefix="/courses",
  tags=["Courses"],
)

@router.get("/", response_model=list[CourseResponse])
async def get_all_courses(db: DBDependency):
  return await course_service.get_all(db)

@router.get("/popular", response_model=list[CourseResponse])
async def get_popular_courses(db: DBDependency):
  return await course_service.get_popular(db)

@router.get("/{id}", response_model=CourseResponse)
async def get_all_courses(id: str, db: DBDependency):
  return await course_service.get_by_id(db, id)

@router.post("/", response_model=CourseResponse)
async def create_course(course: Annotated[CourseRequest, Body()], db: DBDependency):
  return await course_service.create(db, course)
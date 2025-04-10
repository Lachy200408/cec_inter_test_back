from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.config.postgres import init_db, DBDependency
from app.models.tables.course import CourseEntity
from app.routers import course, master, testimony

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(course.router)
app.include_router(master.router)
app.include_router(testimony.router)

@app.on_event("startup")
async def startup():
  init_db()

@app.get("/", description="Redirect to docs")
async def index():
  return RedirectResponse(url="/docs")
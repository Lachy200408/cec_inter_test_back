from typing import Annotated
from app.config.env import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends

connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)

def get_session():
  with Session(engine) as session:
  	yield session

def init_db():
  SQLModel.metadata.create_all(engine)

DBDependency = Annotated[Session, Depends(get_session)]
DBSession = Session
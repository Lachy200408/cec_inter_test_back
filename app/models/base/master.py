from sqlmodel import Field, SQLModel

class MasterBase(SQLModel):
  name: str = Field(title="Nombre del maestro", max_length=50, min_length=3)
  workrole: str = Field(title="Cargo del maestro", max_length=50, min_length=3)
  description: str = Field(title="Descripción del maestro", max_length=250, min_length=5)
  image: str = Field(title="Url de la imagen", max_length=250, min_length=5)
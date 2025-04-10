from sqlmodel import Field, SQLModel

class TestimonyBase(SQLModel):
  name: str = Field(title="Nombre del usuario", max_length=50, min_length=3)
  testimony: str = Field(title="Testimonio", max_length=250, min_length=5)
  image: str = Field(title="Url de la imagen", max_length=250, min_length=5)
  occupation: str = Field(title="Ocupación del usuario", max_length=50, min_length=3)
  rating: int = Field(title="Valoración del testimonio", le=5, ge=0)
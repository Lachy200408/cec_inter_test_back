from sqlmodel import Field, SQLModel

class CourseBase(SQLModel):
  title: str = Field(title="Titulo del curso", max_length=100, min_length=3)
  description: str = Field(title="Descripción del curso", max_length=250, min_length=5)
  degree: str = Field(title="Grado", max_length=25, min_length=3)
  image: str = Field(title="Url de la imagen", max_length=250, min_length=5)
  college: str = Field(title="Nombre de la universidad", max_length=50, min_length=3)
  rating: int = Field(title="Valoración del curso", le=5, ge=0)
  users: int = Field(title="Usuarios del curso", ge=0)
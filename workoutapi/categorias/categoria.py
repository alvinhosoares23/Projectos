from workoutapi.utils.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String


class CategoriaModel(BaseModel):
    __tablename__= "categorias"
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String[50],unique=True, nullable=False)
    user: Mapped['UserModel'] = relationship(back_populates="categoria")
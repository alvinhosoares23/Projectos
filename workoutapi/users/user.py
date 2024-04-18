from workoutapi.utils.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String,DateTime,ForeignKey,Float
from datetime import datetime

class UserModel(BaseModel):
    __tablename__= "users"
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String[50],unique=True, nullable=False)
    cni: Mapped[str] = mapped_column(String[14], nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String[1], nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates="user")
    categoria_id = Mapped[int] = mapped_column(ForeignKey('categoria.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates="user")
    centro_treinamento_id = Mapped[int] = mapped_column(ForeignKey('centro_treinamento.pk_id'))

    
    

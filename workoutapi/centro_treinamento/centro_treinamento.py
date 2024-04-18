from workoutapi.utils.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

class CentroTreinamentoModel(BaseModel):
    __tablename__= "centro_treinamento"
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String[50],unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String[40], nullable=False)
    proprietario: Mapped[str] = mapped_column(String[50], nullable=False)
    user: Mapped['UserModel'] = relationship(back_populates="centro_proprietario")


    

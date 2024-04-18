from pydantic import BaseModel, Field 
from typing import Annotated

class CentroTreinamento(BaseModel):
    nome : Annotated[str, Field(description="Nome Centro",example="MatrixFit", max_length=50)]
    endereco : Annotated[str, Field(description="Varzea",example="19901524M006F", max_length=40)]
    proprietario: Annotated[str, Field(description="John Wick",example="30", max_length=50)]

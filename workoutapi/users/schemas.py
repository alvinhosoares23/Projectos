from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

class User(BaseModel):
    nome : Annotated[str, Field(description="Nome Usuario",example="Pedro", max_length=50)]
    cni : Annotated[str, Field(description="CNI",example="19901524M006F", max_length=14)]
    idade: Annotated[int, Field(description="Idade",example="30")]
    peso : Annotated[PositiveFloat, Field(description="Peso(kg)",example=89)]
    altura : Annotated[PositiveFloat, Field(description="Altura(m)",example=1.80)]
    sexo : Annotated[str, Field(description="Nome Usuario",example="M", max_length=1)]

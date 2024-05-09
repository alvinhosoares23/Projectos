from pydantic import BaseModel, Field 
from typing import Annotated

class Categoria(BaseModel):
    nome : Annotated[str, Field(description="Nome Usuario",example="Pedro", max_length=50)]
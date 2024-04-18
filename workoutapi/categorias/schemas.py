from pydantic import BaseModel, Fields 
from typing import Annotated

class Categoria(BaseModel):
    nome : Annotated[str, Field(description="Nome Usuario",examples="Pedro", max_length=50)]
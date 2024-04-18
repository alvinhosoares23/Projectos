from sqlalchemy import UUID
from sqlalchemy.orm import DeclarationBase,Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as  PG_UUID

class BaseModel(DeclarationBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_UUID=True), default = uuid4, mullable=False)
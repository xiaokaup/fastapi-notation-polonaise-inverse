from decimal import Decimal
from uuid import uuid4, UUID
from sqlmodel import SQLModel, Field


class ResultModel(SQLModel, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    expression: str = Field(nullable=False)
    value: Decimal = Field(nullable=False)

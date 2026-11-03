from pydantic import BaseModel, Field
from uuid import UUID


class TransactionRequest(BaseModel):
    transaction_id: UUID
    amount: float = Field(gt=0)
    currency: str = Field(min_length=3, max_length=3)
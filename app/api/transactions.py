from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.transaction import TransactionRequest
from app.services.fraud_engine import (
    MerchantRules,
    check_business_rules,
)
from app.db.database import get_db
from app.db.models import Transaction as DBTransaction
from app.db.models import Merchant
from app.core.security import get_current_merchant


router = APIRouter(
    prefix="/api/v1/transactions",
    tags=["Transactions"],
)


# Configuration temporaire: ghadi nبدلوها b règles
# personnalisées pour chaque Merchant.
DEFAULT_RULES = MerchantRules(
    max_amount=10000,
    blocked_currencies=[],
)


@router.post("/score")
def score_transaction(
    transaction: TransactionRequest,
    db: Session = Depends(get_db),
    merchant: Merchant = Depends(get_current_merchant),
):
    business_decision = check_business_rules(
        amount=transaction.amount,
        currency=transaction.currency,
        rules=DEFAULT_RULES,
    )

    if business_decision == "REJECT":
        status = "REJECT"
    else:
        status = "REVIEW"

    db_transaction = DBTransaction(
        transaction_id=transaction.transaction_id,
        merchant_id=merchant.id,
        amount=transaction.amount,
        currency=transaction.currency,
        status=status,
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return {
        "transaction_id": str(transaction.transaction_id),
        "merchant_id": str(merchant.id),
        "amount": transaction.amount,
        "currency": transaction.currency,
        "status": status,
        "message": "Transaction saved successfully",
    }
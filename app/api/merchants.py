from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.merchant import MerchantCreate
from app.services.merchant_service import create_merchant


router = APIRouter(
    prefix="/api/v1/merchants",
    tags=["Merchants"],
)


@router.post("/register")
def register_merchant(
    merchant_data: MerchantCreate,
    db: Session = Depends(get_db),
):
    return create_merchant(
        db=db,
        name=merchant_data.name,
    )
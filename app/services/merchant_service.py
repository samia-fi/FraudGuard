from sqlalchemy.orm import Session

from app.db.models import Merchant
from app.core.security import generate_api_key, hash_api_key


def create_merchant(db: Session, name: str):
    api_key = generate_api_key()

    merchant = Merchant(
        name=name,
        api_key_hash=hash_api_key(api_key),
        is_active=True,
    )

    db.add(merchant)
    db.commit()
    db.refresh(merchant)

    return {
        "merchant_id": str(merchant.id),
        "name": merchant.name,
        "api_key": api_key,
        "is_active": merchant.is_active,
    }
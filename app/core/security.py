import secrets
import hashlib

from fastapi import HTTPException, Security, Depends
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Merchant


api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False,
)


def generate_api_key() -> str:
    return "fg_" + secrets.token_urlsafe(32)


def hash_api_key(api_key: str) -> str:
    return hashlib.sha256(
        api_key.encode("utf-8")
    ).hexdigest()


def verify_api_key(api_key: str, stored_hash: str) -> bool:
    return secrets.compare_digest(
        hash_api_key(api_key),
        stored_hash,
    )


def get_current_merchant(
    api_key: str = Security(api_key_header),
    db: Session = Depends(get_db),
):
    if not api_key:
        raise HTTPException(
            status_code=401,
            detail="API Key missing",
        )

    key_hash = hash_api_key(api_key)

    merchant = db.query(Merchant).filter(
        Merchant.api_key_hash == key_hash,
        Merchant.is_active == True,
    ).first()

    if merchant is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key",
        )

    return merchant
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db

router = APIRouter(prefix="/me/offers", tags=["offers"])


@router.get("")
def list_offers(db: Session = Depends(get_db)):
    # TODO: offers for companies the current user follows, filtered through app.filters
    # against the current user's Criteria row. See .claude/contexts/architecture.md "Data model".
    raise NotImplementedError

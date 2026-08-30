from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db

router = APIRouter(prefix="/me/follows", tags=["follows"])


@router.get("")
def list_follows(db: Session = Depends(get_db)):
    # TODO: return current user's followed companies (requires auth dependency)
    raise NotImplementedError


@router.post("/{company_id}")
def follow_company(company_id: int, db: Session = Depends(get_db)):
    # TODO: insert Follow row for current user + company_id
    raise NotImplementedError


@router.delete("/{company_id}")
def unfollow_company(company_id: int, db: Session = Depends(get_db)):
    # TODO: delete Follow row for current user + company_id
    raise NotImplementedError

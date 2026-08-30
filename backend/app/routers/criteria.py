from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db

router = APIRouter(prefix="/me/criteria", tags=["criteria"])


@router.get("")
def get_criteria(db: Session = Depends(get_db)):
    # TODO: return current user's Criteria row (create default if missing)
    raise NotImplementedError


@router.put("")
def update_criteria(db: Session = Depends(get_db)):
    # TODO: upsert current user's Criteria row (allowed_job_names, forbidden_languages, forbidden domains)
    raise NotImplementedError

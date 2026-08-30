from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def register(db: Session = Depends(get_db)):
    # TODO: validate email uniqueness, hash_password(), insert User, return token
    raise NotImplementedError


@router.post("/login")
def login(db: Session = Depends(get_db)):
    # TODO: look up User by email, verify_password(), create_access_token()
    raise NotImplementedError

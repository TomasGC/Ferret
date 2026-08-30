from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Criteria(Base):
    """One row per user. Shape mirrors Engine's criteria.json."""

    __tablename__ = "criteria"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True, nullable=False)
    allowed_job_names: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    forbidden_languages: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)


class CriteriaForbiddenDomain(Base):
    """Junction table: criteria <-> domains (many-to-many), the forbidden ones."""

    __tablename__ = "criteria_forbidden_domains"

    criteria_id: Mapped[int] = mapped_column(ForeignKey("criteria.id"), primary_key=True)
    domain_id: Mapped[int] = mapped_column(ForeignKey("domains.id"), primary_key=True)

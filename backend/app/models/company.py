import enum

from sqlalchemy import String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class AtsPlatform(str, enum.Enum):
    GREENHOUSE = "greenhouse"
    LEVER = "lever"
    WORKDAY = "workday"
    NONE = "none"


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    site: Mapped[str] = mapped_column(String(500), nullable=False)
    ats_platform: Mapped[AtsPlatform] = mapped_column(Enum(AtsPlatform), default=AtsPlatform.NONE)
    ats_token: Mapped[str | None] = mapped_column(String(255), nullable=True)


class CompanyDomain(Base):
    """Junction table: companies <-> domains (many-to-many)."""

    __tablename__ = "company_domains"

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), primary_key=True)
    domain_id: Mapped[int] = mapped_column(ForeignKey("domains.id"), primary_key=True)

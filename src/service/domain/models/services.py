from datetime import timedelta
from enum import Enum
from typing import Any

from sqlalchemy import JSON, VARCHAR

from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column


class ServiceType(str, Enum):
    CAR = "car"
    EQUIPMENT = "equipment"
    HELP = "help"


class Services(BaseModel):
    __tablename__ = "services"

    name: Mapped[str]
    price: Mapped[float]
    description: Mapped[str]
    duration: Mapped[int]
    type: Mapped[ServiceType] = mapped_column(VARCHAR(30))
    options: Mapped[Any] = mapped_column(JSON)

    picture_url: Mapped[str | None]

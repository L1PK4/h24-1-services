from datetime import timedelta
from typing import Any, Self
from pydantic import BaseModel

from service.domain.models.services import ServiceType, Services


class ServiceView(BaseModel):
    id: int
    name: str
    price: float
    description: str
    duration: int
    type: ServiceType
    options: Any

    picture_url: str | None

    @classmethod
    def from_model(cls, model: Services) -> Self:
        return cls(
            id=model.id,
            name=model.name,
            price=model.price,
            description=model.description,
            duration=model.duration,
            type=model.type,
            options=model.options,
            picture_url=model.picture_url,
        )

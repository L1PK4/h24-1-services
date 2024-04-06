from datetime import timedelta
from typing import Any
from pydantic import BaseModel

from service.domain.models.services import ServiceType, Services


class ServiceCommand(BaseModel):

    name: str
    price: float
    description: str
    duration: int
    type: ServiceType
    options: Any

    def to_model(self) -> Services:
        return Services(
            name=self.name,
            price=self.price,
            description=self.description,
            duration=self.duration,
            type=self.type,
            options=self.options,
        )

from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import TypeAdapter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from service.domain.commands.services import ServiceCommand
from service.domain.models.services import Services
from service.domain.views.services import ServiceView
from service.infrastructure.sqlalchemy.repository import (
    ServiceRepository,
    get_repository,
)
from service.infrastructure.sqlalchemy.session_manager import get_session

router = APIRouter(prefix="/api/v1")


@router.get(
    "/services",
    response_model=list[ServiceView],
    responses={
        200: {"model": list[ServiceView], "description": "List of services"},
    },
)
async def get_services(
    repository: Annotated[ServiceRepository, Depends(get_repository)]
) -> list[ServiceView]:
    result = await repository.get_all()
    return [ServiceView.from_model(model) for model in result]


@router.post(
    "/services",
    status_code=200,
    responses={200: {"description": "Location created", "model": ServiceView}},
)
async def create_location(
    service: ServiceCommand,
    repository: Annotated[ServiceRepository, Depends(get_repository)],
) -> ServiceView:
    result = await repository.add(service.to_model())
    return ServiceView.from_model(result)


@router.delete(
    "/services/{entity_id}",
    status_code=200,
    responses={200: {"description": "Location deleted"}},
)
async def delete_location(
    entity_id: int,
    repository: Annotated[ServiceRepository, Depends(get_repository)],
) -> None:
    await repository.delete(entity_id)

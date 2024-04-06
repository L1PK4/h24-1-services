from collections.abc import Sequence
from typing import Annotated
from fastapi import Depends
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from service.domain.models.services import Services
from service.infrastructure.sqlalchemy.session_manager import get_session


class ServiceRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.__session = session

    async def add(self, service: Services) -> Services:
        self.__session.add(service)
        await self.__session.flush()
        return service

    async def delete(self, entity_id: int) -> None:
        q = delete(Services).where(Services.id == entity_id)
        await self.__session.execute(q)

    async def get_all(self) -> Sequence[Services]:
        return (await self.__session.execute(select(Services))).scalars().all()


async def get_repository(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> ServiceRepository:
    return ServiceRepository(session)

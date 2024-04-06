from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    AsyncEngine,
    async_sessionmaker,
)
from sqlalchemy.orm import sessionmaker


class SessionManager:
    def __init__(self):
        self.engine: AsyncEngine | None = None
        self.session_maker: async_sessionmaker[AsyncSession] | None = None

    async def initialize(self, dsn: str) -> None:
        self.engine = create_async_engine(url=dsn, pool_pre_ping=True)
        self.session_maker = async_sessionmaker(
            bind=self.engine, expire_on_commit=False, autoflush=False
        )

    async def close(self) -> None:
        if not self.engine:
            return

        await self.engine.dispose()
        self.engine = None
        self.session_maker = None


session_manager = SessionManager()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    if not session_manager.session_maker:
        raise RuntimeError("Session manager not initialized")

    session = session_manager.session_maker()
    try:
        yield session
    except Exception:
        await session.rollback()
        raise
    else:
        await session.commit()
    finally:
        await session.close()

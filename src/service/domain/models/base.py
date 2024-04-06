from typing import Self, TypeVar
from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel as View

T = TypeVar("T", bound=View)


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @classmethod
    def from_view(cls, view: View) -> Self:
        return cls(**view.model_dump())

    def to_view(self, view_cls: type[T]) -> T:
        return view_cls.model_validate(
            {k: getattr(self, k) for k in inspect(self).__table__.columns}
        )

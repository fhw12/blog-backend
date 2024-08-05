from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import ForeignKey
from sqlalchemy import String


engine = create_async_engine(url="sqlite+aiosqlite:///main.db")
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[String] = mapped_column(String())
    password: Mapped[String] = mapped_column(String())
    role: Mapped[String] = mapped_column(String())


class Post(Base):
    __tablename__ = "posts"

    post_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[String] = mapped_column(String())
    topic: Mapped[String] = mapped_column(String())
    date: Mapped[String] = mapped_column(String())
    description: Mapped[String] = mapped_column(String())
    content: Mapped[String] = mapped_column(String())


async def async_main():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
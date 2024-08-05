from sqlalchemy import select, update, delete
from database.models import async_session
from database.models import User, Post


async def add_user(
    username: str,
    password: str,
    role: str
):
    async with async_session() as session:
        session.add(
            User(
                username=username,
                password=password,
                role=role,
            )
        )
        await session.commit()


async def get_user_by_username(
    username: str
):
    async with async_session() as session:
        return await session.scalar(
            select(User)
                .where(User.username == username)
        )


async def add_post(
    title: str,
    topic: str,
    date: str,
    description: str,
    content: str
):
    async with async_session() as session:
        session.add(
            Post(
                title=title,
                topic=topic,
                date=date,
                description=description,
                content=content,
            )
        )
        await session.commit()


async def get_post_by_id(
    post_id: str
):
    async with async_session() as session:
        return await session.scalar(
            select(Post)
                .where(Post.post_id == post_id)
        )


async def get_all_posts():
    async with async_session() as session:
        return await session.scalars(
            select(Post)
        )
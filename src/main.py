from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.models import async_main
import database.queries as queries


app = FastAPI()

origins = [
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event("startup")
async def startup():
    await async_main()


@app.get('/')
def root():
    return {
        'Server-Name': 'Blog Backend',
    }


@app.get('/post/{post_id}')
async def get_post(post_id: int):
    post = await queries.get_post_by_id(post_id=post_id)

    if post is None:
        return None

    return post


@app.get('/posts')
async def get_all_posts():
    posts = await queries.get_all_posts()

    if posts is None:
        return None

    return list(posts)
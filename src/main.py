from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union

from session_helper import SessionHelper
from database.models import async_main
import database.queries as queries


app = FastAPI()

sessionHelper = SessionHelper()

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


class SignInForm(BaseModel):
    login: str
    password: str


@app.post('/signin')
async def signin(request: SignInForm):
    login = request.login
    password = request.password

    user = await queries.get_user_by_username(username=login)

    if not user:
        return {'message': 'Error login'}

    if user.password != password:
        return {'message': 'Error password'}

    token = sessionHelper.set(username=login)
    return {'message': 'Successfully', 'token': token}


class SignUpForm(BaseModel):
    login: str
    password: str


@app.post('/signup')
async def signup(request: SignUpForm):
    return {'status': 'not implemented'}


class tokenRequest(BaseModel):
    token: Union[str, None]


@app.post('/get-current-user')
async def get_current_user(request: tokenRequest):
    username = sessionHelper.get(request.token)
    user = await queries.get_user_by_username(username=username)

    if username:
        return {
            'username': user.username,
            'role': user.role,
        }
    else:
        return None
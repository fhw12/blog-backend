from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:5500',
    'http://127.0.0.1:5500',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def root():
    return {
        'Server-Name': 'Blog Backend',
    }


@app.get('/post/{post_id}')
def get_post(post_id: int):
    return {
        'id': post_id,
        'title': 'Пост 1',
        'topic': 'Информация',
        'date': '2 Августа, 2024',
        'description': 'Первый пост',
        'content': 'Это первый пост',
    }
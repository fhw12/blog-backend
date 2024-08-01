from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {
        'Server-Name': 'Blog Backend',
    }
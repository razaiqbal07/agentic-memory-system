from fastapi import FastAPI,Request
from contextlib import asynccontextmanager

from app.services.memory import add,init_collection,query

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Application Running"}



@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup logic
    print("App starting...")
    init_collection()

    yield  # app runs here

    # shutdown logic
    print("App shutting down...")


@app.post('/memory')
async def create_memory(req:Request):
    body = await req.json()
    add(body['text'])
    return {
        "success":True
    }

@app.get('/search')
def search(search:str):
    result = query(search)
    return result


from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.services.memory import init_collection
from app.api.router import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

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

from fastapi import APIRouter,Request
from app.services.chat import respond
from app.services.memory_extractor import extract_memory

router = APIRouter(prefix="/chat")

@router.post('/')
async def save(req:Request):
    body = await req.json()
    response = respond(body['text'])
    return {
        "success":True,
        "res": response
    }
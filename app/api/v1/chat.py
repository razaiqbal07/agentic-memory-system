from fastapi import APIRouter,Request
from app.services.chat import respond

router = APIRouter(prefix="/chat")

@router.post('/')
async def save(req:Request):
    body = await req.json()
    respond(body.text)
    return {
        "success":True
    }
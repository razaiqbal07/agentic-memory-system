from fastapi import APIRouter,Request
from app.services.memory import add

router = APIRouter(prefix="/memory")

@router.post('/')
async def save(req:Request):
    body = await req.json()
    add(body.text)
    return {
        "success":True
    }
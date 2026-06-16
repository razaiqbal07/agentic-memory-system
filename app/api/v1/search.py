from fastapi import APIRouter
from app.services.memory import query

router = APIRouter(prefix="/search")

@router.get('/')
def search(search:str):
    result = query(search)
    return result
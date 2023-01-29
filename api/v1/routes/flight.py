from fastapi import APIRouter
from api.utility import response

router = APIRouter()

@router.get('/')
async def base() -> dict:
    body = {}
    msg = "Base Flight endpoint"
    
    return response.default(
        data=body,
        code=200, 
        message=msg
    )
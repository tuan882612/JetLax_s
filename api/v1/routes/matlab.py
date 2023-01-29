from fastapi import APIRouter, Request
from api.utility import response

router = APIRouter()

@router.get('/')
async def base() -> dict:
    body = {}
    msg = "Base Matlab endpoint"
    
    return response.default(
        data=body,
        code=200, 
        message=msg
    )
    
@router.post('/insert')
async def insert(req: Request) -> dict:
    db = req.app.db['flight']
    
    data = dict(req.query_params)
    db.insert_one(data)
    
    return response.default(
        data=data,
        code=201,
        message='You inserted an item'
    )
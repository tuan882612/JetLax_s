from fastapi import APIRouter, Request
from api.utility import response, password
from api.database import mongo
from bson.objectid import ObjectId

router = APIRouter()

@router.get('/')
async def base() -> dict:
    body = {}
    msg = "Base User endpoint"
    
    return response.default(
        data=body,
        code=200, 
        message=msg
    )
    
@router.get('/find')
def get_user(req: Request) -> dict:
    db = req.app.db['user']
    
    query = {'_id': req.query_params['username']}
    out = list(db.find(query))
    
    if len(out) == 0:
        err = 'The user does not exist in the datebase.'
        return response.none(err)

    return response.default(
        data=out[0],
        code=200,
        message=''
    )
    
@router.get('/login')
def log_user(req: Request) -> dict:
    username = req.query_params['username']
    password = req.query_params['password']
   
@router.post('/register')
def reg_user() -> dict:
    return {}
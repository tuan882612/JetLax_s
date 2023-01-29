from fastapi import APIRouter, Request
from api.utility import response

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
async def get_user(req: Request) -> dict:
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
async def log_user(req: Request) -> dict:
    db = req.app.db['user']
    
    query = {'_id': req.query_params['username']}
    out = list(db.find(query))
    
    if len(out) == 0:
        err = 'User does not exist in the database.'
        return response.none(err)
    
    if req.query_params['password'] == out[0]['password']:
        return {'found': True}
    
    return {'found': False}
   
@router.post('/register')
async def reg_user(req: Request) -> dict:
    db = req.app.db['user']
    
    body = await req.json()
    
    query = {'_id': body['_id']}
    out = list(db.find(query))
    
    if len(out) > 0:
        err = 'User already exist in the database.'
        return response.conflict(err)
    
    db.insert_one(dict(body))
    
    return response.created("The user has been inserted into the database.")
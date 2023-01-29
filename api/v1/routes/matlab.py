from fastapi import APIRouter, Request
from api.utility import response

router = APIRouter()

@router.get('/')
async def base() -> dict:
    body = {}
    msg = 'Base Matlab endpoint'
    
    return response.default(
        data=body,
        code=200, 
        message=msg
    )
    
@router.get('/flightinfo')
async def get(req: Request) -> dict:
    db = req.app.db['flight']
    
    query = {'_id': req.query_params['username']}
    out = list(db.find(query))
    
    if len(out) == 0:
        msg = 'The user does not have flight data.'
        return {'detail': msg}
        
    return {'data': out[0]}

@router.post('/insert')
async def insert(req: Request) -> dict:
    db = req.app.db['matlab']
    
    n = db.estimated_document_count()
    data = await req.json()
    
    data = {
        '_id': n+1,
        'data': data['data']
    }
    db.insert_one(data)
    
    return response.created('You inserted an item')
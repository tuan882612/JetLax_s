from fastapi import APIRouter, Request
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
    
@router.get('/find')
async def get(req: Request) -> dict:
    db = req.app.db['flight']
    
    out = list(db.find())
    
    return response.default(
        data=out,
        code=200,
        message=''
    )

@router.post('/create')
async def create(req: Request) -> dict:
    db = req.app.db['flight']
    
    body = await req.json()
    db.insert_one(body)
    
    return response.created('You have created a new flight.')

@router.delete('/remove')
async def remove(req: Request) -> dict:
    db = req.app.db['flight']
    
    if db.estimated_document_count() == 0:
        return response.default(
            data=[],
            code=204,
            message='The user doesnt have any flights.'
        )
        
    query = {
        '_id': req.query_params['username'], 
        'arrivalTime': req.query_params['arrivalTime']
    }
            
    db.find_one_and_delete(query)
    
    return response.default(
        data={},
        code=202,
        message='You have deleted a flight.'
    )
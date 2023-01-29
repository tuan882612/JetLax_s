from fastapi import APIRouter
from api.v1.routes import user, flight, matlab
from api.utility import response

router = APIRouter()

router.include_router(user.router, prefix='/user')
router.include_router(matlab.router, prefix='/matlab')
router.include_router(flight.router, prefix='/flight')

@router.get('/')
async def base() -> dict:
    body = {}
    msg = "Base api endpoint"

    return response.default(
        data=body,
        code=200, 
        message=msg
    )

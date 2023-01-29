def default(
    data: dict, 
    code: int, 
    message: str
) -> dict:
    return {
        "body": data,
        "meta": {
            "status": code,
            "message": message
        }
    }
    
def none(msg: str='') -> dict:
    return default(
        data={},
        code=404,
        message=msg
    )
    
def conflict(msg: str='') -> dict:
    return default(
        data={},
        code=409,
        message=msg
    )
    
def created(msg: str='') -> dict:
    return default(
        data={},
        code=201,
        message=msg 
    )
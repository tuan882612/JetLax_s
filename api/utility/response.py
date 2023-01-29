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
    
def none(msg: str) -> dict:
    return default(
        data={},
        code=404,
        message=msg
    )
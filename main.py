from fastapi import FastAPI
from dotenv import load_dotenv
from api.database import mongo
import uvicorn

from api.v1 import server

load_dotenv()

app = FastAPI()

@app.on_event("startup")
def startup() -> None:
    mongo.setup(app)

@app.on_event("shutdown")
def shutdown() -> None:
    mongo.close(app)

app.include_router(server.router, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run(
        'main:app', 
        host='0.0.0.0', 
        port=1000, 
        reload=True
    )
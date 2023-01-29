from pymongo import MongoClient
from fastapi import FastAPI
import os

def setup(app: FastAPI) -> None:
    url = os.environ['mongo_url']
    app.db = MongoClient(url)['tamu']
    print('Connected to mongodb')
    
def getClient() -> MongoClient:
    url = os.environ['mongo_url']
    db = MongoClient(url)
    return db['tamu']
    
def close(app: FastAPI) -> None:
    app.db.close()
    print('Disconnecting mongodb')
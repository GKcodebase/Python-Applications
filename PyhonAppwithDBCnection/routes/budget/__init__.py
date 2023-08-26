# fast apis for budget
from .schemas import Query
from utils.db import connect
from utils.db import queryDb
from fastapi import APIRouter
from utils.db import queryList
from utils.db import queryUniList
from utils.db.config import configuration

api = APIRouter(prefix ="/api/v1")
config = configuration()
connection = connect(config).get_connection()

@api.post("/query")
async def add_data(query:Query):
    """
        POST API
    """

    try:
        data = queryDb(connection)
    except Exception as e:
        data = None
        print(e)
    return data

@api.get("/query")
async def get_data():
    """
       Get API
    """
    try:
        data = queryList(connection)
    except Exception as e:
        data = None
        print(e)
    return data

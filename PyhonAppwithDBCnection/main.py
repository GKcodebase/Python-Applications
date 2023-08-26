# fast api main page

from fastapi import FastAPI
from routes.budget import api
import uvicorn

api = FastAPI()
api.include_router(api)

@api.get("/")
async def root():
    return {"Status": "online"}

if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000)

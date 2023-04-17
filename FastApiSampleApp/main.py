#  Copyright (c) 2023.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Starting api call
app = FastAPI()

# List to store data.
user_list = []

# User class
class User(BaseModel):
    id: int
    name: str
    email: str
    access: str
    def __hash__(self):  # make hashable BaseModel subclass
        return hash((type(self),) + tuple(self.__dict__.values()))

# Base Url/ detail api
@app.get("/")
def read_root():
    return 'App is running !!!'

# Health api
@app.get("/v1/health")
def read_root():
    return {"Health": "OK"}


# Get user based on id
@app.get("/v1/user/{user_id}")
def read_item(user_id: int):
    if len(user_list) == 0:
        return HTTPException(404, "No user present")
    for user in user_list:
        if user_id == user.id:
            return {"User": user}
    return HTTPException(404, "User Not present")


# Create user api
@app.post("/v1/user")
def create_user(user: User):
    if user:
        user_list.append(user)
        return {"user created", user}
    else:
        return HTTPException(404, "Bad Request")

#  Copyright (c) 2023.

from pydantic import BaseModel

class Query(BaseModel):
    data: str
    where: dict
from pydantic import BaseModel
from typing import List

class request_data(BaseModel):
    numbers: List

class response_data(BaseModel):
    result: List
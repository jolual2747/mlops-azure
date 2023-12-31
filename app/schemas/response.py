from pydantic import BaseModel

class response(BaseModel):
    label: str
    probability: float
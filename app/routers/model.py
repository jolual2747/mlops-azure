from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemas.response import response

model_router = APIRouter()

@model_router.post('/predict', tags = ['predict'], response_model = response)
def predict():
    """Return online prediction for a single row."""
    return JSONResponse(content=jsonable_encoder(response(label="1", probability=1.0)), status_code=200)
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemas.response import response
from app.services.model import ModelService
from app.services.azureconn import AzuremlCon
from app.schemas.raw_data import raw_data
from app.schemas.response import response
from typing import List

model_router = APIRouter()
model_service = ModelService(AzuremlCon(), model_name='heart_disease_model', model_version=3)

@model_router.post('/predict', tags = ['predict'], response_model = response)
def predict(data:raw_data) -> response:
    """Return online prediction for a single row."""
    model_response = model_service.row_prediction(data)
    return JSONResponse(content=jsonable_encoder(model_response), status_code=200)

@model_router.post('/bulk_predict', tags = ['predict'], response_model = List[response])
def bulk_predict(data:List[raw_data]) -> List[response]:
    """Return online prediction for a single row."""
    model_response = model_service.bulk_prediction(data)
    return JSONResponse(content=jsonable_encoder(model_response), status_code=200)
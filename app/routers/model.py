from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemas.response import response
from app.services.model import ModelService
from app.services.azureconn import AzuremlCon
from app.schemas.raw_data import raw_data
from app.schemas.response import response

model_router = APIRouter()
model_service = ModelService(AzuremlCon(), model_name='heart_disease_model', model_version=3)

@model_router.post('/predict', tags = ['predict'], response_model = response)
def predict(data:raw_data) -> response:
    """Return online prediction for a single row."""
    prediction, probability = model_service.row_prediction(data)
    return JSONResponse(content=jsonable_encoder(response(label=str(prediction), probability=probability)), status_code=200)
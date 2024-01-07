from app.schemas.response import response
from app.schemas.raw_data import raw_data
from app.services.model import ModelService
from app.services.azureconn import AzuremlCon
from fastapi.testclient import TestClient
from app.app import app
from typing import List

def test_response():
    """Tests response schema."""
    response_test =  {"label":"1", "probability":0.1} 
    response_schema = response(**response_test)
    assert response_test["label"] == response_schema.label
    assert response_test["probability"] == response_schema.probability

def test_input_data():
    """Tests raw_data schema."""
    raw_data_test = {
        "age":63,
        "sex":1,
        "cp":1,
        "trestbps":145,
        "chol":233,
        "fbs":1,
        "restecg":2,
        "thalach":150,
        "exang":0,
        "oldpeak":2.3,
        "slope":3,
        "ca":0,
        "thal":"fixed"
    }
    raw_data_schema = raw_data(**raw_data_test)
    assert raw_data_test["age"] == raw_data_schema.age 
    assert raw_data_test["sex"] == raw_data_schema.sex 
    assert raw_data_test["cp"] == raw_data_schema.cp 
    assert raw_data_test["trestbps"] == raw_data_schema.trestbps 
    assert raw_data_test["chol"] == raw_data_schema.chol 
    assert raw_data_test["fbs"] == raw_data_schema.fbs 
    assert raw_data_test["restecg"] == raw_data_schema.restecg 
    assert raw_data_test["thalach"] == raw_data_schema.thalach 
    assert raw_data_test["exang"] == raw_data_schema.exang 
    assert raw_data_test["oldpeak"] == raw_data_schema.oldpeak 
    assert raw_data_test["slope"] == raw_data_schema.slope 
    assert raw_data_test["ca"] == raw_data_schema.ca 
    assert raw_data_test["thal"] == raw_data_schema.thal 

def test_model_service():
    """Integration test for model service."""
    model_service = ModelService(
        AzuremlCon(),
        model_name='heart_disease_model', 
        model_version=3
    )
    raw_data_test = {
        "age":63,
        "sex":1,
        "cp":1,
        "trestbps":145,
        "chol":233,
        "fbs":1,
        "restecg":2,
        "thalach":150,
        "exang":0,
        "oldpeak":2.3,
        "slope":3,
        "ca":0,
        "thal":"fixed"
    }
    raw_data_schema = raw_data(**raw_data_test)
    response_model = model_service.row_prediction(raw_data_schema)
    raw_data_schema2 = [raw_data_schema]
    response_model2 = model_service.bulk_prediction(raw_data_schema2)
    assert type(response_model) == response
    for res in response_model2:
        type(res) == response


def test_api():
    """Integration test for most of the components that are used for the app."""

    client = TestClient(app)
    raw_data_test = {
        "age":63,
        "sex":1,
        "cp":1,
        "trestbps":145,
        "chol":233,
        "fbs":1,
        "restecg":2,
        "thalach":150,
        "exang":0,
        "oldpeak":2.3,
        "slope":3,
        "ca":0,
        "thal":"fixed"
        }
    
    raw_data_test2 = [raw_data_test]

    response = client.post(
        'predict',
        json=raw_data_test,
    )
    response2 = client.post(
        'bulk_predict',
        json=raw_data_test2,
    )
    assert response.status_code == 200
    assert response2.status_code == 200
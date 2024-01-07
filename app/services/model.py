from app.schemas.response import response
from app.services.azureconn import AzuremlCon
from app.schemas.raw_data import raw_data
import pandas as pd
from typing import List

class ModelService:
    """Service for Model router to make inference on new data."""
    def __init__(self, con: AzuremlCon, model_name, model_version) -> None:
        self.con = con
        self.model_name = model_name
        self.model_version = model_version
        self.model = self.con.load_model(self.model_name, self.model_version)
    
    def row_prediction(self, data: raw_data) -> response:
        """Makes inference on a sigle row and return label and probabilty in response schema."""
        data_to_predict = pd.DataFrame.from_records([data.model_dump()])
        print(data_to_predict)
        pred = self.model.predict(data_to_predict)[0]
        prob = self.model.predict_proba(data_to_predict)[:,1][0]
        return response(label=str(pred), probability=prob)
    
    def bulk_prediction(self, data: List[raw_data]) -> List[response]:
        """Makes bulk prediction receiving multiple records to make inference on them."""
        records = [row.model_dump() for row in data]
        data_to_predict = pd.DataFrame.from_records(records)
        preds = self.model.predict(data_to_predict)
        probs = self.model.predict_proba(data_to_predict)[:,1]
        responses = [response(label=str(pred), probability=prob) for pred, prob in zip(preds, probs)]
        return responses
from app.schemas.response import response
from app.services.azureconn import AzuremlCon
from app.schemas.raw_data import raw_data
import pandas as pd

class ModelService:
    def __init__(self, con: AzuremlCon, model_name, model_version) -> None:
        self.con = con
        self.model_name = model_name
        self.model_version = model_version
        self.model = self.con.load_model(self.model_name, self.model_version)
    
    def row_prediction(self, data: raw_data):
        data_to_predict = [data.model_dump()]
        pred = self.model.predict(data_to_predict)
        return pred
        



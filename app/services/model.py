from app.schemas.response import response
from app.services.azureconn import AzuremlCon

class ModelService:
    def __init__(self, con: AzuremlCon) -> None:
        self.con = con
    
    def row_prediction(self):
        pass
        



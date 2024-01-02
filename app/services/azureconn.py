from dotenv import load_dotenv
import os
import mlflow
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

class AzuremlCon:
    def __init__(self) -> None:
        load_dotenv('../../secrets.env')
        self.WORKSPACE = os.getenv('WORKSPACE')
        self.WORKSPACE_LOCATION = os.getenv('WORKSPACE_LOCATION')
        self.SUBSCRIPTION_ID = os.getenv('SUBSCRIPTION_ID')
        self.RESOURCE_GROUP = os.getenv('RESOURCE_GROUP')
        self.ml_client = self.get_ml_client()

    def get_ml_client(self):
        ml_client = MLClient(
            DefaultAzureCredential(), self.SUBSCRIPTION_ID, self.RESOURCE_GROUP, self.WORKSPACE
        )
        return ml_client
    
    def set_tracking_uri(self):
        azureml_tracking_uri = self.ml_client.workspaces.get(
            self.ml_client.workspace_name
        ).mlflow_tracking_uri
        mlflow.set_tracking_uri(azureml_tracking_uri)

    def load_model(self, model_name, model_version):
        self.set_tracking_uri()
        model_uri = f"models:/{model_name}/{model_version}"
        return mlflow.pyfunc.load_model(model_uri)
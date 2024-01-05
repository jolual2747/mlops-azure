from utils import add_root_to_path
add_root_to_path()
from app.services.azureconn import AzuremlCon
import pandas as pd
from datetime import date

def read_data(to_predict_path:str) -> pd.DataFrame:
    """Read data from the path where data has been downloaded."""
    return pd.read_csv(to_predict_path)

def predict(model_name:str, model_version:str, predictions_path:str):
    """Make batch prediction on .csv file."""
    to_predict_path = "batch_service/tmp/to_predict.csv"
    con = AzuremlCon()
    model = con.load_model(model_name, model_version)
    df = read_data(to_predict_path)
    df["pred"] = model.predict(df)
    df["prob"] = model.predict_proba(df)[:,1]
    df.to_csv(predictions_path)
    print(f"File for inference saved at {to_predict_path    }")


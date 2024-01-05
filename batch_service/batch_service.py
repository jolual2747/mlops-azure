from feature_pipeline import fetch_data
from predict import predict
from utils import maybe_remove_dir, upload_file_to_azblob
from datetime import date

def batch_service(fetch_data_api:str, path:str, model_name:str, model_version:int):
    """Runs the batch service, fetching data from source, saving it locally and fetch ML models
    from Azure MLflow server."""
    
    # Fetch data to tmp. local folder
    fetch_data(fetch_data_api, path)

    # make batch prediction and store results on local temp
    predictions_path = f"batch_service/tmp/predictions_{date.today().strftime('%Y-%m-%d')}.csv"
    predict(
        model_name=model_name, 
        model_version=model_version, 
        predictions_path=predictions_path
    )

    # Uploads predictions from tmp. to Azure Blob Storage and removes tmp folder
    upload_file_to_azblob(
        local_file_path = path,
        blob_name=predictions_path,
        container_name= "predictions"
    )
    maybe_remove_dir("batch_service/tmp")


if __name__ == "__main__":
    fetch_data_api = "https://mlrawdata123.blob.core.windows.net/rawdata/raw_data.csv"
    model_name = "heart_disease_model"
    model_version = 3
    path = "batch_service/tmp/to_predict.csv"
    batch_service(fetch_data_api, path, model_name, model_version)
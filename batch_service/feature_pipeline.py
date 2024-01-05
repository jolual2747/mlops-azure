from utils import maybe_create_dir, maybe_remove_dir
import pandas as pd

def fetch_data(fetch_data_api, path):
    """Suppose an API to fetch data to predict."""
    
    print("Fetching data from data source...")
    df = pd.read_csv(fetch_data_api)
    maybe_remove_dir("batch_service/tmp")
    maybe_create_dir("batch_service/tmp")
    df.drop(columns=["target"], inplace=True)
    df.to_csv(path, index=False)

if __name__== '__main__':
    fetch_data()
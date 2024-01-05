import os
import shutil
import sys
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def upload_file_to_azblob(local_file_path:str, blob_name:str, container_name:str):
    """Uploads .csv files with predictions to Azure Blob Storage."""

    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    # Create blob_service_client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    try:
        # Get container client
        container_client = blob_service_client.get_container_client(container_name)

        # Uploads file to blob
        with open(local_file_path, "rb") as data:
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.upload_blob(data)

        print("File uploaded succesfully!!!")

    except Exception as ex:
        print("An error occured: ", ex)


def maybe_remove_dir(dirpath: str):
    """Remove a directory if it exists."""
    if os.path.isdir(dirpath):
        shutil.rmtree(dirpath)

def maybe_create_dir(dirpath: str):
    """Create a directory if if does not exists already."""
    if not os.path.isdir(dirpath):
        try:
            os.mkdir(dirpath)
        except FileExistsError:
            pass

def add_root_to_path():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIR = os.path.dirname(ROOT_DIR)
    sys.path.append(PROJECT_DIR)
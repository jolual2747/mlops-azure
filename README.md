# Azure MLOps

This project showcases a comprehensive MLOps pipeline using Azure services. Here's a breakdown of how the project was implemented:

## App
This is the app deployed on Azure Web Apps ready for make inference.

<img src="media/heartdiseaseapp.gif" alt="Heart disease app" width="768" height="432">



## Model Training and Tracking

- Trained a heart disease prediction model using Azure Machine Learning.
- Experiment tracking and model versioning were managed via MLflow, facilitating reproducibility and model comparison.

## API Development with FastAPI

- Implemented a FastAPI-based API to perform real-time inferences.
- Utilized the MLflow registered model hosted on the Azure tracking server, ensuring easy model deployment and inference.

## Streamlit Frontend

- Developed a Streamlit-based user interface, enabling interaction with the API for real-time inference.

## Containerization with Docker

- Created Docker images for each service.
- Uploaded these images to Azure Container Registry, ensuring a centralized repository for container images.

## Deployment with Azure Web App

- Deployed an Azure Web App configured to pull the Docker images from Azure Container Registry and host the application.

## Continuous Integration/Continuous Deployment (CI/CD)

- Established an end-to-end CI/CD pipeline to automate the workflow from running tests to deploying the application upon new changes.

## Scheduled Batch Inference

- Orchestrated a scheduled workflow that fetches and preprocesses data on a monthly basis.
- This workflow then pulls the registered MLflow model from Azure, performs inferences on the records, and uploads the results to Azure Blob Storage.

This project serves as a comprehensive example of MLOps using Azure, covering model training, deployment, CI/CD automation, and scheduled data processing, offering a scalable and efficient approach for machine learning lifecycle management.

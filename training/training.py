from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn import metrics
import pandas as pd
import mlflow
from typing import Tuple, Any

def fetch_data(file_url:str) -> pd.DataFrame:
    """Fetchs data from Azure Blob Storage to train."""
    return pd.read_csv(file_url)

def create_splits(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Splits data between training and test."""
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop("target", axis=1), df["target"], test_size=0.2
    )
    return X_train, X_test, y_train, y_test

def get_transformers(X_train: pd.DataFrame) -> ColumnTransformer:
    """Creates column transformer for feature engineering."""
    num_features = X_train.select_dtypes('number').columns.tolist()
    cat_features = X_train.select_dtypes('object').columns.tolist()
    column_transformer = ColumnTransformer(
        [("OHE", OneHotEncoder(sparse_output=False), cat_features),
        ("scaler", MinMaxScaler(), num_features)
        ]
    ).set_output(transform="pandas")
    return column_transformer

def run_experiment(
        X_train:pd.DataFrame, 
        X_test:pd.DataFrame, 
        y_train:pd.Series, 
        y_test:pd.Series, 
        model:Any, 
        params:dict, 
        experiment_name:str, 
        run_name:str
    ) -> None:
    """Execute a MLflow experiment run for diferent models and params.
    
    Parameters
    ----
    - X_train: Train DataFrame.
    - X_test: Test DataFrame.
    - y_train: Train labels.
    - y_test: Test labels.
    - model: Scikit-learn model class.
    - params: Dict with model params.
    - experiment_name: MLflow experiment name.
    - run_name: Name for the run.
    """
    mlflow.set_experiment(experiment_name = experiment_name)
    with mlflow.start_run(run_name = run_name):
        model_name = model().__class__.__name__
        mlflow.set_tag('model_name',model_name)

        column_transformer = get_transformers(X_train)
        pipe = Pipeline(
            steps = [
                ("transformers", column_transformer),
                (model_name, model(**params))
            ]
        )

        pipe.fit(X_train, y_train)

        y_pred = pipe.predict(X_test)
        y_pred_prob = pipe.predict_proba(X_test)[:,1]

        accuracy = metrics.accuracy_score(y_true=y_test, y_pred=y_pred)
        recall = metrics.recall_score(y_true=y_test, y_pred=y_pred)
        precision = metrics.recall_score(y_true=y_test, y_pred=y_pred)
        auc_score = metrics.roc_auc_score(y_true=y_test, y_score=y_pred_prob)

        mlflow.log_metrics({"test_accuracy": accuracy, "test_recall": recall, "test_precision": precision,
                            "test_auc": auc_score})
        
        mlflow.log_param("penalty", "l2")

        mlflow.sklearn.log_model(pipe, f"heart_disease_{model_name}")
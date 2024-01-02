from pydantic import BaseModel

class raw_data(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: str

    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "age": 14,
                    "sex": "mouse",
                    "cp": "tech",
                    "trestbps": "Wireless mouse for PC",
                    "chol": 4.5,
                    "fbs": 5,
                    "restecg": "Wireless mouse for PC",
                    "thalach": 4.5,
                    "exang": "Wireless mouse for PC",
                    "oldpeak": 4.5,
                    "slope": "Wireless mouse for PC",
                    "ca": 4.5,
                    "thal": "Wireless mouse for PC"
                }
            ]
        }
    }
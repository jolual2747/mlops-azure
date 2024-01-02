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
                    "age":63,
                    "sex":1,
                    "cp":1,
                    "trestbps":145,
                    "chol":233,
                    "fbs":1,
                    "restecg":2,
                    "thalach":150,
                    "exang":0,
                    "oldpeak":2.3,
                    "slope":3,
                    "ca":0,
                    "thal":"fixed"
                }
            ]
        }
    }



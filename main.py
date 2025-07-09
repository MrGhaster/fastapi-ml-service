from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import logging

app = FastAPI()
model = joblib.load("/app/model.pkl")
class_names = ["setosa", "versicolor", "virginica"]

logging.basicConfig(level=logging.INFO)

class InputData(BaseModel):
    features: List[float]

@app.get("/health")
def health_check():
    logging.info("Health check requested")
    return {"status": "OK"}

@app.post("/predict")
def predict(data: InputData):
    logging.info(f"Received prediction request: {data.features}")
    prediction = model.predict([data.features])
    class_index = int(prediction[0])
    class_name = class_names[class_index]
    logging.info(f"Prediction result: {class_index} ({class_name})")
    return {"prediction": class_name}

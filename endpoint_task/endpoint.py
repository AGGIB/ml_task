from fastapi import FastAPI
import random
from pydantic import BaseModel

app = FastAPI()

class Prediction(BaseModel):
    result: str

@app.get("/predict", response_model=Prediction)
def predict():
    forecast = [random.randint(50, 100) for _ in range(5)]
    return {"result": f"Прогноз: {forecast}"}

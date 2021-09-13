from joblib import load
from fastapi import FastAPI
from serviceType import service_type

app = FastAPI()

vector = load("vectors.joblib")
model = load("model.joblib")

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/predict")
async def get_predict(sentimentText: str):
  guard = service_type(sentimentText)
  print(guard)
  text = [sentimentText]
  vec = vector.transform(text)
  prediction = model.predict(vec)
  prediction = str(prediction)
  return {"Sentiment" : sentimentText, "Predict": prediction, "บริการ": guard}
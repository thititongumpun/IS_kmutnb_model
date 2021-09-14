from joblib import load
from fastapi import FastAPI, HTTPException
from serviceType import service_type
from Models.SentimentData import SentimentData
from Service.init_csv import initial_csv
from fastapi.logger import logger

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

@app.post("/data")
async def get_data(sentiment: SentimentData) -> SentimentData:
  logger.info(f"receive data {sentiment}")
  if sentiment is None:
    raise HTTPException(status_code=500, default="Invalid Model")
  data = [sentiment.Sentiment, sentiment.SentimentText]
  await initial_csv(data)
  return sentiment


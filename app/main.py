# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.feature_eng import hash_feature

app = FastAPI()

class PredictionRequest(BaseModel):
    user_id: str
    ad_id: str

@app.get("/")
def read_root():
    return {"status": "alive"}

@app.post("/predict")
def predict(request: PredictionRequest):
    # Basit bir mantık: Hash değerine göre 0 veya 1 dönelim
    try:
        user_hash = hash_feature(request.user_id)
        # Mock model mantığı
        prediction = 1 if user_hash % 2 == 0 else 0
        return {"prediction": prediction, "user_bucket": user_hash}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
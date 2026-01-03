"""
Main API module for Model Serving.
Uses FastAPI to predict ad clicks based on user input.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.feature_eng import hash_feature

app = FastAPI()

class PredictionRequest(BaseModel):
    """
    Prediction request model.
    Expected payload for the /predict endpoint.
    """
    user_id: str
    ad_id: str

@app.get("/")
def read_root():
    """
    Root endpoint to check service health.
    """
    return {"status": "alive"}

@app.post("/predict")
def predict(request: PredictionRequest):
    """
    Prediction endpoint.
    Returns 1 or 0 based on user_id hash logic.
    """
    # Basit bir mantik: Hash degerine gore 0 veya 1 donelim
    try:
        user_hash = hash_feature(request.user_id)
        # Mock model mantigi
        prediction = 1 if user_hash % 2 == 0 else 0
        return {"prediction": prediction, "user_bucket": user_hash}
    except Exception as exc:
        # Pylint 'e' yerine 'exc' gibi acik isimleri sever
        raise HTTPException(status_code=500, detail=str(exc)) from exc

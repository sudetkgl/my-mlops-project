# tests/test_component.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    """
    API'nin beklenen JSON formatına doğru yanıt verip vermediğini test eder.
    """
    payload = {"user_id": "user_xyz", "ad_id": "ad_999"}
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "user_bucket" in response.json()
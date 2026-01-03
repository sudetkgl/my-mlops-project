# smoke_test.py
import requests
import sys
import time

url = "http://localhost:8000/predict"
payload = {"user_id": "smoke_test_user", "ad_id": "smoke_test_ad"}

print("Waiting for service to start...")
time.sleep(5) # Servisin kalkması için kısa bekleme

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("SMOKE TEST PASSED: Service returned 200 OK")
        sys.exit(0)
    else:
        print(f"SMOKE TEST FAILED: Status Code {response.status_code}")
        sys.exit(1)
except Exception as e:
    print(f"SMOKE TEST FAILED: Connection Error - {e}")
    sys.exit(1)
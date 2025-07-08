import requests
import logging

logging.basicConfig(level=logging.INFO)

url = "http://localhost:8000/predict"
payload = {
    "features": [5.1, 3.5, 1.4, 0.2]
}

logging.info(f"Sending request to {url} with payload: {payload}")
response = requests.post(url, json=payload)
logging.info(f"Response status code: {response.status_code}")
logging.info(f"Response body: {response.json()}")

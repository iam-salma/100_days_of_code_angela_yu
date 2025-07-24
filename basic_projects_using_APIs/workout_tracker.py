import os
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

GENDER = "female"
WEIGHT_KG = 62
HEIGHT_CM = 180
AGE = 20

APP_ID = os.environ.get("NUTRITIONIX_APP_ID", "does not exist")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY", "error")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("sheety_endpoint")

nutritionix_params = {
    "query": input("Tell me which exercise you did? : "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

today = datetime.now()

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=headers)
data = response.json()["exercises"][0]

sheety_params = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%X"),
        "exercise": data["user_input"].title(),
        "duration": data["duration_min"],
        "calories": data["nf_calories"]
    }
}

headers = {
    "Authorization": "Basic c2FsbWFzeWVkMTM2MDpTeWVkYWxpMjAwMCE="
}

response = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers)
print(response.text)

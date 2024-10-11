import json

import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = "71"
HEIGHT_CM = "171"
AGE = "27"

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

SHEETY_URL = os.environ["SHEET_ENDPOINT"]
today = str(datetime.today().date())
current_time = datetime.now().time().strftime("%X")

header_sheet = {
"Content-Type": "application/json"

}


for exercise in result["exercises"]:
    sheet_inputs = {
        "sayfa1": {
            "date": today,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": str(exercise["duration_min"]),
            "calories": str(exercise["nf_calories"])
        }
    }


response_sheet = requests.post(url=SHEETY_URL, json=sheet_inputs, headers=header_sheet)
print(response_sheet.text)
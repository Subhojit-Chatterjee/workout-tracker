import requests
import datetime

APP_ID = "4572f8bf"
API_KEY = "b26ed1255fb5882471dd010339b1e45f"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GSHEET_ENDPOINT = "https://api.sheety.co/58e258a8dc59c3b64e72f2ebdc1cf7a1/myWorkouts/workouts"

now = datetime.datetime.now()
date = now.date().strftime("%d/%m/%Y")
time = now.time().strftime("%H:%M:%S")

api_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


query = input("Tell me which exercise you did today: ")

parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 47,
    "height_cm": 155,
    "age": 26,
}

response = requests.post(url=API_ENDPOINT, headers=api_headers, json=parameters)
output_received = response.json()

for exercise in output_received["exercises"]:
    sheet_data = {
        "workout":
            {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
    }
    sheet_response = requests.post(GSHEET_ENDPOINT, json=sheet_data)
sheet_response = requests.get(GSHEET_ENDPOINT)
print(sheet_response.text)

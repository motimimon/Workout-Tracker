import requests
import datetime
time = datetime.datetime
now = time.now()
today = f"{now.day}-{now.month}-{now.year}"

GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 183
AGE = 27

APP_ID = "2b1a80aa"
API_KEY = "383507dad5c5e91449146f970dc60096"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_POST= "https://api.sheety.co/99a9759041b31b9e7a41dc7a1ef44060/workoutBaby/workouts"

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
workout = {
    "workout":
        {
            "date": today,

            "exercise": result["exercises"][0]["name"].title(),
            "duration": result["exercises"][0]["duration_min"],
            "calories": result["exercises"][0]["nf_calories"]
        }
}
new_response = requests.post("https://api.sheety.co/99a9759041b31b9e7a41dc7a1ef44060/workoutBaby/workouts", json= workout)
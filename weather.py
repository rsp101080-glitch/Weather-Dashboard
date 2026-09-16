from dotenv import load_dotenv
import os
import requests
load_dotenv()
API_KEY = os.getenv("API_KEY")
def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    print("Status code:", response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        data = response.json()
        print("Error:", data.get("message", "Something went wrong"))
        return None
def get_forecast(city):

    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

    else:
        data = response.json()
        print("Forecast Error:", data.get("message", "Something went wrong"))
        return None  
    
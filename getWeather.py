import os
import requests

def get_weather():
    latitude = os.environ.get('LAT')
    longitude = os.environ.get('LONG')
    api_key = os.environ.get('API_KEY')

    if not (latitude and longitude and api_key):
        raise ValueError("Latitude, longitude, ou API key manquante")

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    weather_data = get_weather()
    print(weather_data)

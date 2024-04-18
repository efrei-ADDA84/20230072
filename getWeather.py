from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

#Creation de la route 
@app.route('/')
def get_weather():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    api_key = os.environ.get('API_KEY')

    if not (latitude and longitude and api_key):
        raise ValueError("Veuillez indiquer la latitude, longitude et l'API key")

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

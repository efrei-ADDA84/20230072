from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


api_key = '6e1c179eb50ae7f95cc2d7845ad8b6ec'



@app.route('/weather', methods=['GET'])
def get_weather():
    latitude = request.args.get('LATTITUDE')  
    longitude = request.args.get('LONGITUDE')  

    if not (latitude and longitude):
        return jsonify({"error": "Veuillez fournir la latitude et la longitude"}), 400  

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data), 200  
    else:
        return jsonify({"error": "Impossible de récupérer les données météo"}), 500 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

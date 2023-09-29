from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Configure CORS for the '/main' and '/weather' endpoints
cors = CORS(app, resources={r"/weather": {"origins": "*"}})

@app.route('/weather')
def get_weather():
    load_dotenv()
    api_key = os.getenv('WEATHER_KEY')  # Replace with your API key
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    if not lat or not lng:
        return {'error': 'Latitude and longitude are required parameters.'}

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    if weather_data.get('status') == 'OK':
        weather_info = weather_data['results'][0]['name']
        print(weather_info)
        return {'location': f'Lat: {lat}, Lng: {lng}', 'weather': weather_info}
    else:
        return {'error': 'Could not fetch weather data.'}
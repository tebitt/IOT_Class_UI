from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Configure CORS for the '/main' and '/weather' endpoints
cors = CORS(app, resources={r"/rain": {"origins": "*"}, r"/temp": {"origins": "*"}})

@app.route('/rain')
def get_rainfall():
    load_dotenv()
    api_key = os.getenv('WEATHERBIT_KEY')  # Replace with your API key
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    if not lat or not lng:
        return {'error': 'Latitude and longitude are required parameters.'}

    weather_url = f'https://api.weatherbit.io/v2.0/forecast/daily?lat={lat}&lon={lng}&key={api_key}'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    if weather_data:
        return {'percip': weather_data['data'][0]['pop']}
    else:
        return {'error': 'Could not fetch weather data.'}
    
@app.route('/temp', methods=['GET'])
def get_temp():
    load_dotenv()
    api_key = os.getenv('WEATHER_KEY')  # Replace with your API key
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    if not lat or not lng:
        return {'error': 'Latitude and longitude are required parameters.'}

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}&units=metric'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    if weather_data:
        return {'temp': weather_data['main']['temp'], 'feels': weather_data['main']['feels_like']}
    else:
        return {'error': 'Could not fetch weather data.'}
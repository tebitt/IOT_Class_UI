from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import os
import numpy as np
import pandas as pd
from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Configure CORS for the '/main' and '/weather' endpoints
cors = CORS(app, resources={r"/rain": {"origins": "*"}, r"/temp": {"origins": "*"}, r"/bus": {"origins": "*"}})

@app.route('/rain')
def get_rainfall():
    load_dotenv()
    api_key = os.getenv('WEATHERBIT_KEY')  # Replace with your API key
    lat = os.getenv('SAMYAN_LAT')
    lng = os.getenv('SAMYAN_LNG')
    # lat = request.args.get('lat')
    # lng = request.args.get('lng')

    if not lat or not lng:
        return {'error': 'Latitude and longitude are required parameters.'}



    # weather_url = f'https://api.weatherbit.io/v2.0/forecast/daily?lat={lat}&lon={lng}&key={api_key}'
    # weather_response = requests.get(weather_url)
    # weather_data = weather_response.json()
    
    # percip = weather_data['data'][0]['pop']
    # location = weather_data['city_name']
    percip = 50
    location = 'Pathum Wan'
    if percip < 50:
        msg = 'Rain warning'
    elif percip >= 50 and percip < 75:
        msg = 'Moderate rain warning'
    elif percip >= 75:
        msg = 'Heavy rain warning'
    else:
        msg = 'Clear skies' 

    return {'percip': percip, 'location' : location, 'msg': msg}
    # if weather_data:
    #     return {'percip': percip, 'location' : location, 'msg': msg}
    # else:
        # return {'error': 'Could 5 fetch weather data.'}

@app.route('/temp', methods=['GET'])
def get_temp():
    load_dotenv()
    api_key = os.getenv('WEATHER_KEY')  # Replace with your API key
    lat = os.getenv('SAMYAN_LAT')
    lng = os.getenv('SAMYAN_LNG')
    # lat = request.args.get('lat')
    # lng = request.args.get('lng')


    if not lat or not lng:
        return {'error': 'Latitude and longitude are required parameters.'}

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}&units=metric'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    if weather_data:
        print(type(weather_data['main']['temp']))
        return {'temp': round(weather_data['main']['temp']), 'feels': round(weather_data['main']['feels_like'])}
    else:
        return {'error': 'Could not fetch weather data.'}
    
@app.route('/bus')
def bus_info():
    df = pd.read_csv('buss.csv', header=None)
    df['Bus_No'] = df[0].str.split(' ').str[0]

    sample = df.sample(1)
    data = pd.DataFrame(columns=['Bus_No', 'Destination', 'ETA'])
    data['Bus_No'] = sample['Bus_No']
    data['Destination'] = sample[2].str.strip()
    # random time from 1 to sample[4]
    data['ETA'] = np.random.randint(1, sample[4])
    #assign new row index
    data.index = range(len(data))
    # turn into  dictionary
    output = dict()
    for i, d in enumerate(data.to_dict('records')):
        output[i] = d
    return output[0]

if __name__ == '__main__':
    app.run(port='5000', debug=True)
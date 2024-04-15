from flask import Flask, request, jsonify
import requests
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

appWeather = Flask(__name__)

@appWeather.route('/gettingWeather', methods=['GET'])
def gettingWeather():
    APIKEY_openweather = request.args.get('API_KEY')
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    # Logging the request details
    logging.info(f"The weather for lat = {lat}, lon = {lon}, and API key = {APIKEY_openweather} is requested.")

    if not (lat and lon):
        logging.error("Missing latitude or longitude in the request.")
        return jsonify({"error": "Missing latitude or longitude"}), 400

    full_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY_openweather}"
    response = requests.get(full_url)

    if response.status_code == 200:
        data = response.json()
        weather = data.get('weather', [{}])[0]
        # Logging the successful retrieval of weather
        logging.info(f"Weather data retrieved: {weather}")
        return jsonify(weather)
    else:
        # Logging the error with fetching weather data
        logging.error(f"Failed to fetch weather data, status code {response.status_code}.")
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

if __name__ == "__main__":
    appWeather.run(debug=True)

from flask import Flask, request, jsonify
import requests
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

appWeather = Flask(__name__)

@appWeather.route('/')
def gettingWeather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    api_key = os.getenv('API_KEY')
    dns_name_label = os.getenv('DNS_NAME_LABEL')

    # Check if essential parameters are available
    if not (lat and lon and api_key and dns_name_label):
        logging.error("Missing parameters: latitude, longitude, API key, or DNS name label.")
        return jsonify({"error": "Missing parameters"}), 400

    full_url = f"http://{dns_name_label}.francecentral.azurecontainer.io/?lat={lat}&lon={lon}&API_KEY={api_key}"
    response = requests.get(full_url)

    if response.status_code == 200:
        data = response.json()
        logging.info(f"Weather data retrieved: {data}")
        return jsonify(data)
    else:
        logging.error(f"Failed to fetch weather data, status code {response.status_code}.")
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

if __name__ == "__main__":
    appWeather.run(host='0.0.0.0', port=5000, debug=True)

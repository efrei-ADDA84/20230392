import os
import sys
import unittest
from flask_testing import TestCase

# Set the path to include the 'src' folder where 'gettingWeather.py' is located
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from gettingWeather import appWeather  # Import the Flask app

class TestWeatherApp(TestCase):
    def create_app(self):
        # Configure the app for testing
        appWeather.config['TESTING'] = True
        appWeather.config['DEBUG'] = False
        return appWeather

    def test_weather_route_exists(self):
        response = self.client.get('/gettingWeather?lat=40.712776&lon=-74.005974&API_KEY=048a8f361dd3ae83d166d41cd7767b74')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

import os
import sys
import unittest
from flask_testing import TestCase

# Add the src directory to sys.path to find the appWeather module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.gettingWeather import appWeather  # Import the Flask app

class TestWeatherApp(TestCase):
    def create_app(self):
        # Configure the app for testing
        appWeather.config['TESTING'] = True
        appWeather.config['DEBUG'] = False
        return appWeather

    def test_weather_route_exists(self):
        # Ensure the route is accessible
        response = self.client.get('/gettingWeather?lat=40.712776&lon=-74.005974&API_KEY=048a8f361dd3ae83d166d41cd7767b74')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

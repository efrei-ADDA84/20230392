import requests
import json
import os

def gettingWeather(lat, lon):

    APIKEY_openweather = '048a8f361dd3ae83d166d41cd7767b74'
    full_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY_openweather}"


    #with io.StringIO() as f:
    r = requests.get(full_url)

    data = json.loads(r.content.decode('utf-8'))
    
    return data['weather'][0]

if __name__ == "__main__":

    lat = os.getenv('lat', default = 0)
    lon = os.getenv('lon', default = 0)

    weather = gettingWeather(lat, lon)

    print('The weather for lat = ', lat, ' and lon = ', lon, ' is : ')
    print(json.dumps(weather, indent = 4))
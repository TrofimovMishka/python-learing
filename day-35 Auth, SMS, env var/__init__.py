# API Authentication
import requests
from smsservice import main

WEATHER_API_KEY = '$$$$'  # it takes 2 hours for key activation.
URL = 'https://api.openweathermap.org/data/2.5/weather'
URL_FORECAST = 'https://api.openweathermap.org/data/2.5/forecast'
# URL = 'https://api.openweathermap.org/data/3.0/onecall'

params = {
    "lat": 58.853130,
    # "lat": 52.409538,
    "lon": 5.732710,
    # "lon": 16.931992,
    "appid": WEATHER_API_KEY,
    "units": "metric",
    "mode": "JSON",
    "cnt": 4,
    "lang": "ua"
}

response = requests.get(url=URL_FORECAST, params=params)
response.raise_for_status()
#
# weather_data = {'cod': '200', 'message': 0, 'cnt': 4, 'list': [{'dt': 1712836800, 'main': {'temp': 16.01, 'feels_like': 14.95, 'temp_min': 16.01, 'temp_max': 16.66, 'pressure': 1032, 'sea_level': 1032, 'grnd_level': 1021, 'humidity': 49, 'temp_kf': -0.65}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'clouds': {'all': 18}, 'wind': {'speed': 5.22, 'deg': 249, 'gust': 6.86}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-04-11 12:00:00'}, {'dt': 1712847600, 'main': {'temp': 16.53, 'feels_like': 15.49, 'temp_min': 16.53, 'temp_max': 16.96, 'pressure': 1031, 'sea_level': 1031, 'grnd_level': 1020, 'humidity': 48, 'temp_kf': -0.43}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 63}, 'wind': {'speed': 4.41, 'deg': 257, 'gust': 6.67}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-04-11 15:00:00'}, {'dt': 1712858400, 'main': {'temp': 13.37, 'feels_like': 12.36, 'temp_min': 13.37, 'temp_max': 13.37, 'pressure': 1030, 'sea_level': 1030, 'grnd_level': 1020, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 93}, 'wind': {'speed': 3.34, 'deg': 276, 'gust': 8.13}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-04-11 18:00:00'}, {'dt': 1712869200, 'main': {'temp': 13.19, 'feels_like': 12.13, 'temp_min': 13.19, 'temp_max': 13.19, 'pressure': 1031, 'sea_level': 1031, 'grnd_level': 1021, 'humidity': 60, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 3.26, 'deg': 268, 'gust': 7.85}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-04-11 21:00:00'}], 'city': {'id': 3088171, 'name': 'Poznań', 'coord': {'lat': 52.4095, 'lon': 16.932}, 'country': 'PL', 'population': 570352, 'timezone': 7200, 'sunrise': 1712808170, 'sunset': 1712857392}}
weather_data = response.json()

print(weather_data)

# if weather condition code < 700 print("Bring umbrella") list.weather.id

# {print("Bring umbrella") for (k, v) in weather_data["list"]}
# print(weather_data["list"][0]["weather"][0]["id"])

is_will_rainy = False

# for hour_data in weather_data["list"]:
#     code = hour_data["weather"][0]["id"]
#     if code < 700:
#         is_will_rainy = True

# if is_will_rainy:
#     print("Bring umbrella")

hours_where_rainy = [[j for weather in j if weather["id"] < 700] for j in [i["weather"] for i in weather_data["list"]]]

if len(hours_where_rainy) > 0:
    print("Bring umbrella")
    main.send_sms_notification("Bring umbrella, it could be rainy")



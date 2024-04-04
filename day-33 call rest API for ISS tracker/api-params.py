URL = 'http://api.sunrise-sunset.org/json'
from datetime import datetime

# coordinates get from here: https://www.latlong.net/convert-address-to-lat-long.html
import requests

parameters = {
    "lat": 51.919437,
    "lng": 19.145136,
    "formatted": 0
}
response = requests.get(URL, params=parameters)
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(data)
print(f'sunrise = {sunrise}')
print(f'sunset = {sunset}')

time_now = datetime.now()
print(f'now = {time_now}')

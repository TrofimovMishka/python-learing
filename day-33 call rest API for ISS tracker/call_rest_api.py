# ISS - International Space Station
# API - Application Programing Interface
ISS_GET_POSITION = 'http://api.open-notify.org/iss-now.json'

import requests
from position import PositionOfISS

response = requests.get(url=ISS_GET_POSITION)
print(response.status_code)
if response.status_code != 200:
    pass
    # Error
# The same way:
response.raise_for_status() # if status no 200 exception will be thrown
data = response.json()
# print(type(data)) # dict

iss_position = PositionOfISS(data["iss_position"]["latitude"], data["iss_position"]["longitude"], data["timestamp"])

print(iss_position.get_latitude())
print(iss_position.get_longitude())
# use https://www.latlong.net/Show-Latitude-Longitude.html to visual show position under the Earth


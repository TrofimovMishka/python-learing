import smtplib
from datetime import datetime

import requests

MY_LAT = 51.919437  # My latitude
MY_LONG = 19.145136  # My longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.

def is_iss_under():
    return abs(MY_LAT - iss_latitude) < 5 > abs(MY_LONG - iss_longitude)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def is_now_dark():
    return sunset <= time_now.hour <= sunrise


def send_notification():
    GMAIL = 'smtp.gmail.com'
    PORT = 587
    mail_from = 'mykhailo.trofimov@gmail.com'
    mail_to = 'hamann.trofimov@gmail.com'
    app_pass = 'to generate in google account'

    with smtplib.SMTP(host=GMAIL, port=PORT) as connection:
        connection.starttls()
        connection.login(mail_from, password=app_pass)
        print("Try send an email")
        connection.sendmail(mail_from, mail_to, msg="Subject: ISS notification\n\n\nISS under your location - looked up to the sky")


if is_iss_under() and is_now_dark():
    send_notification()
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

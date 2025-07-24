# An Application Programming Interface (API) is a set of commands, functions, protocols, and objects that programmers
# can use to create software or interact with an external system.
# errors: 1XX : Hold On ; 2XX : Here you Go ; 3XX : Go away ; 4XX : You Screwed Up ; 5XX : I Screwed Up ;

import os
import requests
import smtplib
import time
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

MY_LAT = 17.385044
MY_LONG = 78.486671
email = os.getenv('SMTP_EMAIL')
password = os.getenv('SMTP_PASSWORD')

PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    # data = response.json()["iss_position"]["longitude"]  or
    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude:
        return True

def is_night():
    # https://api.sunrise-sunset.org/json?lat=17.385044&lng=78.486671
    response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")
    sunset = data["results"]["sunset"].split("T")[1].split(":")

    hour = datetime.now().hour
    if hour >= sunset or hour <= sunrise:
        return True

while True:
    time.sleep(60)  # run the code every 60 seconds.
    # If the ISS is close to my current position and it is currently dark
    if is_iss_overhead() and is_night():
        # Then email me to look up.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )

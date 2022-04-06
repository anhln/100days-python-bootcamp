import requests
from twilio.rest import Client
import os
from os.path import join, dirname
from dotenv import *

URL = "https://api.openweathermap.org/data/2.5/onecall"
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
auth_token = os.environ.get("AUTH_TOKEN")
my_phone = os.environ.get("MOBILE_PHONE")
account_sid = "AC70cd152a51beea71ea4fe746c60fbbd7"

parameters = {
    "lat": 26.140289,#21.027763,
    "lon": 91.791862, #105.834160,
    "exclude" : "current, minutely, daily",
    "appid": API_KEY
}
next_12hours_weather = []

response = requests.get(URL, params=parameters)
if response.status_code == 200:
    data = response.json()
    hour_data = data["hourly"]
    next_12hours = hour_data[0:12]
    next_12hours_weather = [item["weather"][0] for item in next_12hours]
    # print(next_12hours_weather)
    will_rain = False
    for item in next_12hours_weather:
        if item["id"] < 700:
            will_rain = True
    if will_rain:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body='Bring an umbrella',
            from_='+17577988291',
            to= my_phone
        )

        print(message.sid)
else:
    print(response.status_code)
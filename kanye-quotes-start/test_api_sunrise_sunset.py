import requests
import datetime as dt
import smtplib
import time

MY_CITY_LAT = "21.027763"
MY_CITY_LNG = "105.834160"
URL = "https://api.sunrise-sunset.org/json"
URL_ISS = "http://api.open-notify.org/iss-now.json"

parameters = {
    "lat": MY_CITY_LAT,
    "lng": MY_CITY_LNG,
    "formatted": 0
}

iss_lat = ""
iss_long = ""


def is_iss_overhead():
    global iss_lat, iss_long
    res = requests.get(URL_ISS)
    if res.status_code == 0:
        dt = res.json()
        iss_lat = dt["iss_position"]["latitude"]
        iss_long = dt["iss_position"]["longtitude"]

        if MY_CITY_LAT-5 < iss_lat < MY_CITY_LAT+5 and MY_CITY_LNG-5 < iss_long < MY_CITY_LNG+5:
            return True


def is_night():
    """check if time is night"""
    response = requests.get(URL, params=parameters)
    if response.status_code == 200:
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        now = dt.datetime.now()

        if now.hour < sunrise or now.hour > sunset:
            return True

def send_email(content, email):
        my_email = "lenguyenanh08091985@gmail.com"
        smtp_server = "smtp.gmail.com"
        msg = "Subject: ISS watching \n\n" + content

        with smtplib.SMTP(smtp_server) as connection:
            connection.starttls()
            connection.login(user=my_email, password="LeHoang@1984")
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=msg)
            print("ok")
            connection.close()

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        # send an email
        print("In here")
        send_email("Please go out and watch up the sky!", "anhlnster@gmail.com")


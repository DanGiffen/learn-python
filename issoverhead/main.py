import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 52.674160 # Your latitude
MY_LONG = -0.302540 # Your longitude
FROM_EMAIL = "chimpfinch@gmail.com"
TO_EMAIL = "dangiffen@gmail.com"
PASSWORD = "lyjl pksm rbrm wjuz"

def iss_above():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])
    # tests whether iss values between two other values
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def dark_outside():
    time_now = datetime.now()
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()
    # can split on first character and then split again on a specific index on the resultant list.
    # So here split on "T" and then index 1 on ":" and select the 1st index in the list
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

    if time_now.hour >= sunset or time_now.hour < sunrise:
        return True


while True:
    # while True will continue to run until stopped. sleep set to slow cycle down to 60 secs
    time.sleep(60)
    if iss_above() and dark_outside():
        with smtplib.SMTP("smtp.gmail.com")as connection:
            subject = "Look UP!"
            contents = "The ISS is above you"

            connection.starttls()
            connection.login(user=FROM_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=FROM_EMAIL,
                                to_addrs=TO_EMAIL,
                                msg=f"{subject}\n{contents}")








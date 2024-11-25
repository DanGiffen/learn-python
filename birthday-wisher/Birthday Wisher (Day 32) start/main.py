import smtplib
import datetime as dt
import random

MY_EMAIL = "chimpfinch@gmail.com"
PASSWORD = "bqnk pgxo sqdu cvpz"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:

    with open(file="quotes.txt") as file:
        quotes = file.readlines()

        subject = "Be Positive"
        message = random.choice(quotes)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="dangiffen@gmail.com",
                                msg=f"Subject:{subject}\n\n{message}"
                                )


import smtplib
import datetime as dt
import random


def get_quote():
    file_quote = open("quotes.txt")
    list_quotes = file_quote.readlines()
    file_quote.close()
    return random.choice(list_quotes)


def send_email():
    my_email = "lenguyenanh08091985@gmail.com"
    smtp_server = "smtp.gmail.com"
    msg = "Subject: \n\n" + get_quote()

    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(user=my_email, password="LeHoang@1984")
        connection.sendmail(from_addr=my_email,
                            to_addrs="anhlnster@gmail.com",
                            msg=msg)
        connection.close()
# use the date time

now = dt.datetime.now()
today = now.weekday()
if today < 5:
    send_email()
print(now)
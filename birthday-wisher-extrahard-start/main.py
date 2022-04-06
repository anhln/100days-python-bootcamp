##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas

from os import listdir
from os.path import isfile, join
import random
import smtplib


def generate_email(name):
    # read files in a folder
    path = "letter_templates"
    # choose a file and return an email
    templates = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    letter_file = random.choice(templates)
    with open(letter_file) as file:
        letter = file.read().replace("[NAME]", name)
    return letter

# 4. Send the letter generated in step 3 to that person's email address.

def send_email(name, email):
    content_email = generate_email(name)
    print(content_email)
    my_email = "lenguyenanh08091985@gmail.com"
    smtp_server = "smtp.gmail.com"
    msg = "Subject: test \n\n"+content_email

    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(user=my_email, password="LeHoang@1984")
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=msg)
        print("ok")
        connection.close()

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.today()
birthdays_data = pandas.read_csv("birthdays.csv")
birthdays_list = birthdays_data.values.tolist()
for item in birthdays_list:
    name, email, year, month, day = item
    if month == today.month and day == today.day:
        send_email(name, email)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv




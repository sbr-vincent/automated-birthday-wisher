##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Get all the information from birthday
data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
month = now.month
day = now.day

birthday_list = data.to_records(index=False)
for birthday in birthday_list:
    # 2. Check if today matches a birthday in the birthdays.csv
    if birthday[3] == month and birthday[4] == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        letter = random.randint(1, 3)
        with open(f"./letter_templates/letter_{letter}.txt") as card:
            birthday_letter = card.read()
            new_letter = birthday_letter.replace("[NAME]", birthday[0])
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday[1],
                msg=f"Subject:Happy Birthday!!!\n\n{new_letter}"
            )

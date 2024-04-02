##################### Hard Starting Project ######################
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import datetime as dt
import random
import pandas
import smtplib

FILE = 'birthdays.csv'
PLACEHOLDER = "[NAME]"
TODAY = dt.datetime.now()
HOST = 'smtp.gmail.com'
PORT = 587
APP_PASS = 'cybu ceza kybd gpjy'
MY_EMAIL = 'mykhailo.trofimov@gmail.com'
def send_mail(email, subject, message):
    with smtplib.SMTP(host=HOST, port=PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASS)
        connection.sendmail(MY_EMAIL, email, msg=f'Subject: {subject} \n\n\n {message}' )

raw_data = pandas.read_csv(FILE)
todays_persons = raw_data[(raw_data["day"] == TODAY.day) & (raw_data["month"] == TODAY.month)]

for person in todays_persons.to_dict(orient="records"):
    name = person["name"]
    mail = person["email"]
    template_path = f'letter_templates/letter_{random.choice([1, 2, 3])}.txt'

    with open(template_path) as file:
        template = file.read()
        new_letter = template.replace(PLACEHOLDER, name)
        send_mail(mail, f"Happy birthday dear {name}", new_letter)

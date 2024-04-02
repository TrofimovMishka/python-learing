import datetime as dt
import random

import my_email

QUOTES_TXT = "quotes.txt"

current_date = dt.date
current_time = dt.time

today_date_time = dt.datetime

print(current_time.min)
print(current_date.today())
print(today_date_time.now())
print(today_date_time.month)  # return <attribute 'month' of 'datetime.date' objects> How return integer???

weekday = today_date_time.now().isoweekday() # iso - sunday is 1
wk = today_date_time.now().weekday() # sunday is 0
# print(wk)
# print(weekday)

# Create date_time obj
specific_date_time = dt.datetime(year=191, month=12, day=1, hour=14, minute=34, second=54)
# print(specific_date_time)

if wk == 0: # send only in sunday
    with open(QUOTES_TXT) as file:
        try:
            data = file.readlines()

        except FileNotFoundError:
            print(f"Error: File {QUOTES_TXT} no found")
        else:
            # print(type(data))
            row = random.choice(data)
            print(f'This row will be send to user: {row}')
            my_email.send_mail(row, 'Test from python app', 'hamann.trofimov@gmail.com')

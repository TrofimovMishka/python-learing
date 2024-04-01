import datetime as dt

current_date = dt.date
current_time = dt.time

now = dt.datetime

print(current_time.min)
print(current_date.today())
print(now.now())
print(now.month) # return <attribute 'month' of 'datetime.date' objects> How return integer???

# weekday = now.isoweekday() # doesnt work
# weekday = now.weekday() # doesnt work
# print(weekday)

# Create date_time obj
specific_date_time = dt.datetime(year=191, month=12, day=1, hour=14, minute=34, second=54)
print(specific_date_time)

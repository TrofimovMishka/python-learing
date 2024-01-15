def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = month_days[month - 1]
    if is_leap(year) and days == 28:
        return days + 1
    else:
        return days


# 🚨 Do NOT change any of the code below
year = 2023  # Enter a year
month = 5  # Enter a month
days = days_in_month(year, month)
print(days)

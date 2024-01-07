print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
persons = int(input("How many people to spit the bill? "))

# Solution: round to .XX

total_bill = (bill * tip_percentage) / 100 + bill

result = round(total_bill / persons, 2)

print(f"each person should pay: ${result}")

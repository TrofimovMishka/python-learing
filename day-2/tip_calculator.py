print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
persons = int(input("How many people to spit the bill? "))

# Solution: round to .XX

total_bill = (bill * tip_percentage) / 100 + bill

result = total_bill / persons

#The same output for all print: How round numbers in py

print(f"each person should pay: ${round(result, 2)}") # round this: 10232.06831212 to this 10232.07, AND this 12.6 to 12.6
print("%.2f" % result) # round this: 10232.06831212 to this 10232.07 AND this 12.6 to 12.60
print("{:.2f}".format(result)) # round this: 10232.06831212 to this 10232.07 AND this 12.6 to 12.60

print("%.3f" % result) # round this: 10232.06831212 to this 10232.068 AND this 12.6 to 12.60
print(("{:.4f}".format(result))) # round this: 10232.06831212 to this 10232.0683  AND this 12.6 to 12.60

import csv

# with open("weather_data.csv") as file:
#     items = file.readlines()
#     for i in items:
#         print(i.strip()) # -> day,temp,condition

with open("weather_data.csv") as file:
    data = csv.reader(file)
    temp = []
    for row in data:
        print(row) # -> ['day', 'temp', 'condition']
        # temp.append(row[1]) #-> ['temp', '12', '14', '15', '14', '21', '22', '24']
        if row[1] != 'temp':
            temp.append(row[1])

print(temp)
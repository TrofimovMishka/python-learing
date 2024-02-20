import pandas

COUNT_CSV = "squirrel_count.csv"
SQUIRREL_DATA_CSV = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"



all_sq = pandas.read_csv(SQUIRREL_DATA_CSV)

column_1 = 'Primary Fur Color'

cinn = len(all_sq[all_sq["Primary Fur Color"] == 'Cinnamon'])
gray = len(all_sq[all_sq["Primary Fur Color"] == 'Gray'])
black = len(all_sq[all_sq["Primary Fur Color"] == 'Black'])

print(cinn)
print(gray)
print(black)

count = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Count": [cinn, gray, black]
}

frame = pandas.DataFrame(count)
frame.to_csv(COUNT_CSV)
import pandas

# pandas - lib for data analysis and manipulation tool - link: https://pandas.pydata.org/docs/

data = pandas.read_csv("../weather_data.csv")

print(data)

print(type(data)) # <class 'pandas.core.frame.DataFrame'> - like whole table

print(data["temp"]) # only this column print

print(type(data["temp"])) # <class 'pandas.core.series.Series'> - like one

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(sum(temp_list)/len(temp_list)) # average temp
print(data["temp"].mean()) # average temp

#how use collumn name:
print(data["temp"].max()) # max from temperature column
# or
print(data.temp.max())

# Get data in Row:
print(data[data.day == "Monday"]) # return row where day is Monday. return DataFrame

print(data[data.temp == data.temp.max()]) # return row where temp is maximum. return DataFrame

print(data[data.temp == data.temp.max()].day) # return day where temp is maximum.

monday_temp = (data[data.day == "Monday"].temp * 9/5) + 32 # monday temp in F
print(monday_temp)

# Create DataFrame from scratch

data_new = {
    "students" : ["a", "b", "c"],
    "scores": [1, 2, 4]
}
# format to DataFrame
new_frame = pandas.DataFrame(data_new)
#Write to csv - if no existing - will be created
new_frame.to_csv("new_file.csv")

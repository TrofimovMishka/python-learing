# List comprehension example  - is how create list from list:

numbers = [num for num in range(1, 200, 5)]
print(numbers)

new_list = [num + 1 for num in numbers]  # list comprehension
print(new_list)

letters = [w.upper() for w in "Angela"]  # ['A', 'N', 'G', 'E', 'L', 'A']

numbers = [i for i in range(1, 30) if i > 20]  # [21, 22, 23, 24, 25, 26, 27, 28, 29]

result = [int(n) for n in numbers if int(n) % 2 == 0]

print(numbers.__contains__(22))

# Dictionary comprehension:
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {k: len(k) for k in sentence.split()}
print(result) # {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
def to_far(num):
  return (num * 9/5) + 32

weather_f = {k:to_far(v) for (k, v) in weather_c.items()}
print(weather_f) # {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}

# with open("file1.txt") as file_1:
#   lines_1 = [int(w.strip()) for w in file_1.readlines()]
#  # print(lines_1)
#
# with open("file2.txt") as file_2:
#   lines_2 = [int(w.strip()) for w in file_2.readlines()]
#  # print(lines_2)
#
# result = [n for n in lines_1 if lines_2.__contains__(n)] => mine solution

# result = [num for num in list1 if num in list2] => solution from school
#
#
# # Write your code above 👆
# print(result)

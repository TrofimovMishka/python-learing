print("Hello in day 5\n")

student_heights = ["Apples", "Pear", "Lemon"]

print(student_heights)

for fruit in student_heights:
    print(f"{student_heights.index(fruit)} - {fruit}")

avg = 158.33333333333334
sum = 5334


print(f'total height = {sum}\nnumber of students = {len(student_heights)}\naverage height = {round(avg)}')


student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

tmp = 0

for num in student_scores:
    if num > tmp:
        tmp = num

print(tmp)
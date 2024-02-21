
import pandas

st = {
    "student": ["bob", "rob", "gray"],
    "score": [1, 3, 5]
}

frame = pandas.DataFrame(st)
# print(frame)

#How loop throuh:

# for (k, v) in frame.items():
#     print(k) # => column name

# Inbuild pandas solution:
for (index, row) in frame.iterrows():
    # print(row) # pandas Series obj
    print(row.student) # result from column student
    print(row.score) # result from column score
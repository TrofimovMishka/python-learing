ALPHABET_CSV = "nato_phonetic_alphabet.csv"
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# Solution without pandas
# with open(ALPHABET_CSV) as file:
#     nato =[w.strip() for w in file.readlines()[1:]]
#     dict_form = { k.split(",")[0]:k.split(",")[1] for k in nato}

# Solution with pandas:
data = pandas.read_csv(ALPHABET_CSV)
dict_form = {row.letter: row.code for (index, row) in data.iterrows()}
# print(dict_form)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.



is_input_incorrect = True

while is_input_incorrect:
    user_input = input("Enter a word: ").upper()
    try:
        result = [dict_form[w] for w in user_input]
    except KeyError:
        print("Sorry, only letters please")
    else:
        print(result)
        is_input_incorrect = False

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

names_path = "Input/Names/invited_names.txt"
starting_letter_path = "Input/Letters/starting_letter.txt"
output_letters_path = "Output/ReadyToSend/"

with open(starting_letter_path, mode="r") as temp:
    template = temp.read()

with open(names_path) as names:
    all_names = names.readlines()

for n in all_names:
    name = n.replace("\n", "")
    new_letter = template.replace(PLACEHOLDER, name)

    with open(output_letters_path + "letter_for_" + name + ".txt", mode="w") as output:
        output.write(new_letter)

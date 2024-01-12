import random


# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
def lets_start():
    print('welcome to HANGMAN game!')


lives = 9
word_list = ['baboon', 'fruit', 'happiness', 'looser', 'expectations']
user_input = ''
chosen_word = random.choice(word_list)
chosen_word_array = []


def is_live():
    return lives > 0


def gues_a_letter():
    global user_input
    user_input = input('Guess a letter: ').lower()


def output_guessed_letters():
    global lives

    for i in range(1, len(chosen_word) + 1):
        letter_in_word = chosen_word[i - 1]
        if user_input == letter_in_word:
            chosen_word_array.pop(i-1)
            chosen_word_array.insert(i - 1, user_input)

    print(chosen_word_array)


def fill_array():
    for i in range(1, len(chosen_word) + 1):
        chosen_word_array.append("_")
    print(chosen_word_array)


def is_letter_in():
    return chosen_word.__contains__(user_input)


lets_start()
print(chosen_word)

fill_array()

while is_live():
    global lives
    gues_a_letter()
    output_guessed_letters()
    if not is_letter_in():
        lives -= 1

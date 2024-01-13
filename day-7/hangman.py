import random
import hangman_art
import hangman_words
import os
from time import sleep


def lets_start():
    print(hangman_art.logo)
    print('\n')


lives = 6
user_input = ''
chosen_word = random.choice(hangman_words.word_list)
chosen_word_array = []


def is_live():
    return lives >= 0


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


fill_array()

while is_live():
    sleep(0.5)
    os.system('clear')

    lets_start()
    output_guessed_letters()
    print(hangman_art.stages[lives])
    gues_a_letter()

    if not is_letter_in():
        print(f'You choose letter [{user_input}], that not in word, that means you loose live')
        sleep(1.5)
        lives -= 1
    if lives < 0:
        print('You loose')

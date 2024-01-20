import art
import art2
import game_data
import random
import os

compare = ''
against = ''
final_score = 0
is_game = True
is_user_win = False
user_choice = ''


def logo():
    print(art2.logo)


def clear_screen():
    os.system('clear')


def ask_user_choice():
    global compare, against, user_choice

    compare = random.choice(game_data.data)
    against = random.choice(game_data.data)

    print(f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}")
    print(art2.vs)
    print(f"Against B: {against['name']}, a {against['description']}, from {against['country']}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()


def start_game():
    clear_screen()
    logo()
    ask_user_choice()


def game():
    global is_user_win, final_score, is_game

    is_user_loose()
    while is_game:
        clear_screen()

        logo()
        you_right()
        ask_user_choice()

        is_user_loose()


def is_user_loose():
    global is_user_win, is_game, final_score
    if user_choice == 'a':
        is_user_win = compare['follower_count'] > against['follower_count']
    elif user_choice == 'b':
        is_user_win = compare['follower_count'] < against['follower_count']
    if not is_user_win:
        clear_screen()
        logo()
        print(f"Sorry. that's wrong. Final score: {final_score}")
        is_game = False


def you_right():
    global final_score
    final_score += 1
    print(f"You're right. Current score: {final_score}")


start_game()
game()

import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
comp_cards = []


############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def get_card():
    return random.choice(cards)


def prepare_start_cards():
    user_cards.append(get_card())
    user_cards.append(get_card())
    comp_cards.append(get_card())
    comp_cards.append(get_card())


def get_winner():
    user_score = sum(user_cards)
    comp_score = sum(comp_cards)

    print(f"Your final band: {user_cards}")
    print(f"Computer's final band: {comp_cards}")

    if 21 != comp_score < user_score <= 21:
        print(f"You win with score {user_score}")
    else:
        print(f"You loose, computer score {comp_score} > your score {user_score}")


def is_anyone_have_blackjack():
    if ((user_cards.__contains__(11) and user_cards.__contains__(10))
            or (comp_cards.__contains__(11) and comp_cards.__contains__(10))):
        get_winner()
        return True
    else:
        return False


is_lets_play = input("Do you want to play a game of Blackjack? Type 'y' or 'N': ").lower() == 'y'

if is_lets_play:
    print(art.logo)
    prepare_start_cards()
    print(f"Your cards: {user_cards}")
    print(f"Computers first card: {comp_cards[0]}")

def game():
    global is_lets_play
    while is_lets_play:

        if is_anyone_have_blackjack():
            is_lets_play = False
            break

        if (sum(user_cards) > 21) and user_cards.__contains__(11):
            user_cards.remove(11)
            user_cards.append(1)

            if sum(user_cards) > 21:
                print("You loose")
                break
            else:
                user_cards.remove(1)
                user_cards.append(11)

        is_next_card = input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y'

        if is_next_card:
            game()
        else:
            comp_cards.append(random.choice(cards))
            if sum(comp_cards) > 21:
                print(f"You win, computer has score = {sum(comp_cards)} over 21")
                break
            get_winner()
            is_lets_play = False


game()

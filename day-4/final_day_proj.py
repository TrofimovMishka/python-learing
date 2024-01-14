import random
user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Rock - kamen, Scissors - nozycy

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]

print("Your chose: ")
# print(list[user_chose])

comp_chose = random.randint(0, 2)

print("Computer chose: ")
print(list[comp_chose])

again = 'Again'
comp_win = "You lose"
user_win = 'You win'

outcomes = {
    (0, 0): again,
    (0, 1): comp_win,
    (0, 2): user_win,
    (1, 0): user_win,
    (1, 2): comp_win,
    (2, 0): comp_win,
    (2, 1): user_win
}

print(outcomes.get((user_chose, comp_chose), 'Invalid'))

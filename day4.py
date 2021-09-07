print("\n                 ==========Day 4==========")
print("\n           ==========Randomization and Lists==========")
print("\n\n           ==========Rock Paper Scissors==========")
import random

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
game_images = [rock, paper, scissors]
while 1>0:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0: 
        print("You typed an invalid number, you lose!") 
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

import random

random_integer = random.randint(0,20)
print(f"\nRandom integer = {random_integer}\n")

random_float = random.random()
print(f"\nRandom float = {random_float}\n")

random_large_float = random_integer * random_float
print(f"\nRandom mixed number = {random_large_float}\n")


face = random.randint(0,1)
#?print(face)
if face == 0:
    print("Tails")
else:
    print("Heads")
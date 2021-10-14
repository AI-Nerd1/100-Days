#!/usr/bin/env python3

################### Scope ####################
import random
logo = """

                                                                    
                                                                    
    ,---,                                       ,---,      ,----,   
  .'  .' `\                                  ,`--.' |    .'   .' \  
,---.'     \                                /    /  :  ,----,'    | 
|   |  .`\  |                              :    |.' '  |    :  .  ; 
:   : |  '  |  ,--.--.        .--,         `----':  |  ;    |.'  /  
|   ' '  ;  : /       \     /_ ./|            '   ' ;  `----'/  ;   
'   | ;  .  |.--.  .-. | , ' , ' :            |   | |    /  ;  /    
|   | :  |  ' \__\/: . ./___/ \: |            '   : ;   ;  /  /-,   
'   : | /  ;  ," .--.; | .  \  ' |            |   | '  /  /  /.`|   
|   | '` ,/  /  /  ,.  |  \  ;   :            '   : |./__;      :   
;   :  .'   ;  :   .'   \  \  \  ;            ;   |.'|   :    .'    
|   ,.'     |  ,     .-./   :  \  \           '---'  ;   | .'       
'---'        `--`---'        \  ' ;                  `---'          
                              `--`                                  

                                                                    
"""

print(logo)
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

number = random.randint(1,101)
print("Welcome to Number Guessing Game")
level = input("Choose a difficulty; Type 'easy' or 'hard': ")
level = level.lower()


print(f"Number = {number} ")
def easy_mode():
    easy_count = 10
    game_over = False
    while game_over is False:
        print(f"You have {easy_count} attempts remaining to guess the number")
        easy_count = easy_count - 1
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high")
            if easy_count > 0:
                print("Guess again")
        if guess < number:
            print("Too low")
            if easy_count > 0:
                print("Guess again")
        if guess == number:
            print("You win!!")
            game_over = True
        if easy_count == 0:
            print("You ran out of attempts")
            print("Game Over!")
            game_over = True

def hard_mode():
    hard_count = 5
    game_over = False
    while game_over is False:
        print(f"You have {hard_count} attempts remaining to guess the number")
        hard_count = hard_count - 1
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high")
            if hard_count > 0:
                print("Guess again\n")
        if guess < number:
            print("Too low")
            if hard_count > 0:
                print("Guess again\n")
        if guess == number:
            print("You win!!")
            game_over = True
        if hard_count == 0:
            print("You ran out of attempts")
            print("Game Over!")
            game_over = True
        
if level == "easy":
    easy_mode()
if level == "hard":
    hard_mode()


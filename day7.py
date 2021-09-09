# print("\n                 ==========Day 7==========")
# print("\n                 ==========Hangman==========")

# #!  _
# #! | |
# #! | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
# #! | '_ \ / _` | '_ \ / _` | '_ ` _  \/ _` | '_ \  
# #! | | | | (_| | | | | (_| | | | | | | (_| | | | |
# #! |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
# #!                     __/ |
# #!                    |___/


      


#Step 1 
import random
from hangman_art import logo1, stages
from hangman_words import word_list

print(logo1) 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# import random
# display = []
# chosen_word = random.choice(word_list)
# print(chosen_word)
# length = len(chosen_word)
# unique = set(chosen_word)
# unique_len = len(unique)
# count = 0
# for x in range(length):
#         display.append("_")
#print(display)



# while count < unique_len:
#     guess = input("Guess a letter: ").lower()
    
    #TODO-1: - Create an empty List called display.

    #TODO-2: - Loop through each position in the chosen_word;

    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

    # for position in range(length):
    #     letter = chosen_word[position]
    #     if letter == guess:
    #         display[position] = letter
        
    # if guess not in chosen_word:
    #     state = stages[-position]
       
    # print(display)
    # print(state)
    # count += 1


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

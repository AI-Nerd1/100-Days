print("\n                 ==========Day 3==========")
print("\n           ==========Conditional Statements==========")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")


print("\n           ==========Odd or even==========")
variable = int(input("Enter the number : "))
if (variable % 2) == 0:
    print(f"{variable} is an even number.")
else:
    print(f"{variable } is an odd number.")

print("\n           ==========BMI Calculator 2.0==========")
print("Welcome to the advanced Body-Mass Index Calcualator")
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight/ (height ** 2)

if BMI < 18.5:
    status = "underweight."
elif BMI > 18.5 and BMI < 25:
    status = "normal."
elif BMI > 25 and BMI < 30:
    status = "Slightly overweight."
elif BMI > 30 and BMI < 35:
    status = "obese."
elif BMI > 35:
    status = "clinically obese."

print(f"Your Body Mass Index is {round(BMI)} and this indicates that you are {status}")


print("\n           ==========Leap year check==========")
year = int(input("What year: "))
by_4 = year%4
by_100 = year%100
by_400 = year%400
if year%4==0 or year%100 != 0 and by_400 % 2 == 0:
    print(f"{year} is a Leap year!.")
else:
    print(f"{year} is not a Leap year")



print("\n           ==========Python Pizza==========")
print("           Welcome to Python Pizza")
print("      Menu:\nSmall Pizza:                            $ 15\nMedium pizza:                           $ 20\nLarge Pizza:                            $ 25")
print("Pepperoni for Small pizza:              $  2\nPepperoni for Medium and Large Pizza:   $  3")
print("Extra cheese for any size pizza:        $  1")

print("           Please place your order")
pizza_size = input("What size of pizza do you want? S, M or L: ")
pep = input("Do you want pepperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if(pizza_size == "S" or pizza_size == "s"):
    bill += 15
    if pep == "Y" or pep == "y":
        bill += 2
    if cheese == "Y" or cheese == "y":
        bill += 1
if(pizza_size == "M" or pizza_size == "m"):
    bill += 20
    if pep == "Y" or pep == "y":
        bill += 3
    if cheese == "Y" or cheese == "y":
        bill += 1
if(pizza_size == "L" or pizza_size == "l"):
    bill += 25
    if pep == "Y" or pep == "y":
        bill += 3
    if cheese == "Y" or cheese == "y":
        bill += 1
print(f"Your bill is ${round(bill)}.00\n     Thank you for patronizing us")
    

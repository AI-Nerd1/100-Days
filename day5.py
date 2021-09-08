print("\n                 ==========Day 5==========")
print("\n                 ==========Loops==========")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for x in days:
    print(x)

print("\n                 ==========Height Average==========")
height = [180, 124, 165, 173, 189, 169, 146]
sum = 0
count = 0
for x in height:
    sum += x
    count += 1

ave = sum / count
print(f"Average Height of {count} students = {round(ave)}")


print("\n                 ==========Highest Score==========")
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for x in student_scores:
    if x > highest_score:
        highest_score = x

print(f"The highest score in the class is: {highest_score}")



print("                     ===========Even number Calculator===========")
# for x in range(0, 10):
#     print(x)
even = 0
for x in range(0, 101, 2):
    even += x

print(even)

print("            ===========Fizz Buzz Generator===========")
for x in range (1, 101):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


print("            ===========Password Generator Project===========")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("     Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))

#*Eazy Level - Order not randomised:
#*e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password1 = []
for x in range(nr_letters):
    E_password = random.choice(letters)
    password1.append(E_password)
for x in range(nr_symbols):
    E_password = random.choice(numbers)
    password1.append(E_password)
for x in range(nr_numbers):
    E_password = random.choice(symbols)
    password1.append(E_password)


password = "".join(password1)


#!Hard Level - Order of characters randomised:
#?e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passcode1 = []
for x in range(nr_letters):
    H_password = random.choice(letters)
    passcode1.append(H_password)
for x in range(nr_symbols):
    H_password = random.choice(symbols)
    passcode1.append(H_password)
for x in range(nr_numbers):
    H_password = random.choice(numbers)
    passcode1.append(H_password)

random.shuffle(passcode1)
passcode = "".join(passcode1)

print(f"Your suggested easy pass code is: {password}")
print(f"Your suggested hard pass code is: {passcode}")
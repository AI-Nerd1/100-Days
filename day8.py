print("\n                 ==========Day 4==========")
print("\n           ==========Simple Function==========")
def greet():
  print("Hello Angela")
  print("How do you do Jack Bauer?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Jack Bauer")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")


#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")

print("\n           ==========Area Calculator==========")
def paint_calc(height, width, cover):
    cans = round((height*width)/cover)
    print(cans)

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

print("\n           ==========Prime Number checker==========")
def prime_check(n):
    if n == 2:
        print("It is a prime number")
    elif n == 3:
        print("It is a prime number")
    elif n == 5:
        print("It is a prime number")
    elif n == 1:
        print("It is a prime number")
    elif (n%2 != 0) and (n%3 != 0) and(n%5 != 0) and(n%7 != 0):
        print("It is a prime number")
    else:
        print("It is not a prime number")
n = int(input("Enter Prime Number: "))
prime_check(n)

print("\n           ==========caesar-cipher-1==========")

def ceaser_cipher(alphabet, direction, text, shift):
    if direction == "encode":
        for x in text:
            y = alphabet[x] - shift
            crypt.append(y)
    "".join(crypt)
    print(crypt)
    if direction == "decode":
        for x in text:
            y = alphabet[x] + shift
            decrypt.append(y)
    "".join(decrypt)
    print(decrypt)

def encrypt(alphabet, text, shift):
    encryption = ""
    for x in text:
        position = alphabet.index(x)
        new_position = position + shift
        new_letter = alphabet[new_position]
        encryption += new_letter
    print(f"Encrypted message is: {encryption}")

def decrypt(alphabet, text, shift):
    decryption = ""
    for x in text:
        position = alphabet.index(x)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decryption += new_letter
    print(f"Decrypted message is: {decryption}")

def cipher():
    if direction == "encode":
        encrypt(alphabet, text, shift)

    if direction == "decode":
        decrypt(alphabet, text, shift)

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z',
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
 '!', '#', '$', '%', '&', '(', ')', '*', '+',
 ' ' ,'a', 'b', 'c', 'd', 'e', 
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
'!', '#', '$', '%', '&', '(', ')', '*', '+']

def caeser(alphabet, text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift = shift * -1
    for x in text:
        position = alphabet.index(x)
        new_position = position + shift
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"The {direction}d text is: {end_text}")


check = True
while check is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    caeser(alphabet, text, shift, direction)
    next = input("To try again, tap Y, else tap N: ").lower()
    if next == "n":
        check = False
        print("Encryption Ended")



print("            ===========Password Generator and encryptor Project===========")
import time
import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z',
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
 '!', '#', '$', '%', '&', '(', ')', '*', '+',
 ' ' ,'a', 'b', 'c', 'd', 'e', 
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
'!', '#', '$', '%', '&', '(', ')', '*', '+']

count = 0
shift = random.randint(1, 9)
for x in range(1000000):
    start = time.time()
    passcode = []
    for x in range(100):
        password = random.choice(alphabet)
        passcode.append(password)

    random.shuffle(passcode)
    passcode = "".join(passcode)
    encryption = ""
    for x in passcode:
        position = alphabet.index(x)
        new_position = position + shift
        new_letter = alphabet[new_position]
        encryption += new_letter
    count +=1
    print(f"{passcode}")
    print(f"{encryption}")
    
print(f"Generated {count} samples")
print(f"Shift used = {shift}")   
end = time.time()
taken = end - start
print(f"Time of execution = {taken}")

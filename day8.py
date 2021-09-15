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



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caeser(alphabet, text, shift, direction)

next = input("To try again, tap Y, else tap N: ").lower()
check = True
while check is True:
    if next == "y":
        caeser(alphabet, text, shift, direction)
    else:
        check = False


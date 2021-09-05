print("\n                 ==========Day 2==========")
print("\n                 ==========Data Types==========")
print("Hello"[4])
print(1_234)
name = 3.1415
print(type(name))

new_name = str(name)
print(len(new_name))

num = 1234
print(type(num))
str_num = str(num)
print(type(str_num))
float_num = float(num)
print(type(float_num))
bool_num = bool(num)
print(type(bool_num))


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
if len(two_digit_number)  != 2:
    print("Input not 2 digits")
else:
    string_2_digit_number = str(two_digit_number)
    print("First digit = ",string_2_digit_number[0])
    print("Second digit = ",string_2_digit_number[1])
    first_digit = string_2_digit_number[0]
    second_digit = string_2_digit_number[1]
    int_first_digit = int(first_digit)
    int_second_digit = int(second_digit)
    print("Sum of",int_first_digit, "and" ,int_second_digit, "=",int_first_digit + int_second_digit)

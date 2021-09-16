# print("\n                 ==========Day 9==========")
# print("\n           ==========Python Dictionaries==========")

logo = '''
                  ___________
                  \         /
                   )_______(
                   |"""""""|_.-._,.---------.,_.-._
                   |       | | |               | | ''-.
                   |       |_| |_             _| |_..-'
                   |_______| '-' `'---------'` '-'
                   )"""""""(
                  /_________\\
                .-------------.
               /_______________\\
'''
print(logo)

empty_dictionary = {}
empty_dictionary["First define"] = "Initial defination of the contents of a library"
empty_dictionary["Second define"] = "Second definition of the contents of a library"
for x in empty_dictionary:
    print(x)
    print(f"{x}: {empty_dictionary[x]}")


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades ={}
for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80 and student_scores[student] < 91:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 70 and student_scores[student] < 81:
        student_grades[student] = "Acceptable"
    elif student_scores[student] < 71:
        student_grades[student] = "Fail"

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)

##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]



travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


def add_new_country(country, times, places):
    cities = []
    log = {}
    cities.append(places)
    log["country"] = country
    log["visits"] = times
    log["cities"] = places
    travel_log.append(log)


country = input("What country have you travelled to: ")
times = int(input("How many times?: "))
places = input("What cities did you travel to?: ")

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country(country, times, places)
print(travel_log)
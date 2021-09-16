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


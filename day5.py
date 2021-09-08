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
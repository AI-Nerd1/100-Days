print("\n                 ==========Day 5==========")
print("\n                 ==========Loops==========")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for x in days:
    print(x)

print("\n                 ==========Height Average==========")
height = [180, 124, 165, 173, 189, 169, 146]
sum = 0
for x in height:
    sum = sum + x

ave = sum / len(height)
print(f"Average Height of {len(height)} students = {round(ave)}")
#!/usr/bin/env python3
logo = "TURTLE"

from turtle import*

logan = Turtle()
logan.shape("turtle")
logan.color("red")
for x in range(4):
    logan.forward(100)
    logan.right(90)
    logan.forward(100)



color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(179)
    if abs(pos()) < 1:
        break
end_fill()
done()

my_screen = Screen()
my_screen.bgcolor("white")
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Country",["USA", "Russia", "UK", "Nigeria", "Canada"])
table.add_column("Capital", ["America", "Moscow","London", "Abuja", "B Columbia"])

print(table)
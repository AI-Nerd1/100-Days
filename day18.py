#!/usr/bin/env python3
from turtle import Turtle, Screen

cursor = Turtle()

screen = Screen()

cursor.shape("turtle")
cursor.color("red")

def red_square():
    for x in range(4):
            cursor.fd(100)
            cursor.lt(90)


for x in range(10):
    cursor.fd(200)
    cursor.lt(90)
    cursor.fd(10)
    cursor.lt(90)
    cursor.fd(200)
    cursor.rt(45)
    cursor.fd(10)
    cursor.rt(90)

red_square()
cursor.ht()


bot = Turtle()
bot.shape("turtle")
bot.color("green")

for x in range(20):
    bot.fd(10)
    bot.pu()
    bot.fd(5)
    bot.pd()


screen.exitonclick()
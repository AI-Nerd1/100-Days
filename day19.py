#!/usr/bin/env python3
import random
import turtle
from turtle import Turtle, Screen

bot = Turtle()
screen = Screen()
screen.screensize(2000, 1500)
bot.color("white")
bot.pencolor("red")

colors = ["darkblue", "DarkOrange","LawnGreen", "MediumVioletRed",
"Salmon", "DeepSkyBlue", "Red", "Yellow", "green",
"orange", "indigo","Blue"]

def move_forward():
    bot.pencolor(random.choice(colors))
    bot.fd(10)

def move_backwards():
    bot.pencolor(random.choice(colors))
    bot.bk(10)

def move_left():
    bot.pencolor(random.choice(colors))
    new_heading = bot.heading() + 10
    bot.setheading(new_heading)
    # bot.lt(45)
    # bot.fd(10)

def move_right():
    bot.pencolor(random.choice(colors))
    new_heading = bot.heading() + 10
    bot.setheading(new_heading)
    # bot.rt(45)
    # bot.fd(10)

def clear_screen():
    bot.clear()
    bot.pu()
    bot.home()
    bot.pd()

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = move_right)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "c", fun = clear_screen)







screen.exitonclick()

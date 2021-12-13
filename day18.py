#!/usr/bin/env python3
from turtle import Turtle, Screen

cursor = Turtle()

screen = Screen()
bot = Turtle()
# bot.shape("arrow")
bot.color("white")

# cursor.shape("turtle")
# cursor.color("red")

# def red_square():
#     for x in range(4):
#             cursor.fd(100)
#             cursor.lt(90)

# for x in range(10):
#     cursor.fd(200)
#     cursor.lt(90)
#     cursor.fd(10)
#     cursor.lt(90)
#     cursor.fd(200)
#     cursor.rt(45)
#     cursor.fd(10)
#     cursor.rt(90)

#red_square()
cursor.ht()

# bot.pencolor("red")
# for x in range(20):
#     bot.fd(10)
#     bot.pu()
#     bot.fd(5)
#     bot.pd()
# bot.pu()
# bot.home()

def traces():
    for x in range(10):
        bot.fd(5)
        bot.pu()
        bot.fd(5)
        bot.pd()

def triangle():
    bot.pencolor("red")
    for x in range(3):
        # bot.fd(50)
        traces()
        bot.rt(120)
    bot.home()

def square():
    bot.pencolor("blue")
    for x in range(4):
        traces()
        bot.rt(90)
    bot.home()

def pentagon():
    bot.pencolor("yellow")
    for x in range(5):
        traces()
        bot.rt(72)
    bot.home()

def hexagon():
    bot.pencolor("green")
    for x in range(6):
        traces()
        bot.rt(60)
    bot.home()

def heptagon():
    bot.pencolor("orange")
    for x in range(7):
        traces()
        bot.rt(51.5)
    bot.home()

def octagon():
    bot.pencolor("brown")
    for x in range(8):
        traces()
        bot.rt(45)
    bot.home()

def nonagon():
    bot.pencolor("grey")
    for x in range(9):
        traces()
        bot.rt(40)
    bot.home()

def decagon():
    bot.pencolor("pink")
    for x in range(10):
        traces()
        bot.rt(36)
    bot.home()


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()



screen.exitonclick()
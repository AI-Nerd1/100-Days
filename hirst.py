#!/usr/bin/env python3
import colorgram
import random
import turtle
bot = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(2000,1500)
bot.speed("fastest")
bot.pensize(1)
bot.color("white")
turtle.colormode(255)

colors = ["darkblue", "DarkOrange","LawnGreen", "MediumVioletRed",
 "Salmon", "DeepSkyBlue", "Red", "Yellow", "green",
  "orange", "indigo","Blue"]

# colors = colorgram.extract("hirst.jpeg", 5)
# color_tuple = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)
#     color_tuple.append(new_color)
# print(color_tuple)
def forward_paint():
    for times in range(33):
        bot.pencolor(random.choice(colors))
        bot.pd()
        bot.dot(10)
        bot.pu()
        bot.fd(30)
        

def turn_left():
    for x in range(2):
        bot.lt(90)
        bot.fd(20)
    forward_paint()

def turn_right():
    for x in range(2):
        bot.rt(90)
        bot.fd(20)
    forward_paint()

for x in range(20):
    turn_right()
    turn_left()
   
    

screen.exitonclick()
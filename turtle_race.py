#!/usr/bin/env python3
import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(height = 500, width = 1000)
screen.bgcolor("skyblue")
screen.title("TURTLE RACE!")

bot1 = Turtle()
bot2 = Turtle()
bot3 = Turtle()
bot4 = Turtle()
bot5 = Turtle()

bot1.shape("turtle")
bot2.shape("turtle")
bot3.shape("turtle")
bot4.shape("turtle")
bot5.shape("turtle")

bot1.color("grey", "red")
bot2.color("grey","orange")
bot3.color("grey","yellow")
bot4.color("grey","green")
bot5.color("grey","blue")

bot1.pu()
bot1.goto(-450, 0)
bot1.pd

bot2.pu()
bot2.goto(-450, 50)
bot2.pd

bot3.pu()
bot3.goto(-450, 100)
bot3.pd

bot4.pu()
bot4.goto(-450, -50)
bot4.pd

bot5.pu()
bot5.goto(-450, -100)
bot5.pd

user_bet = turtle.textinput(title = "Betting site", prompt = "Who would win?:")
print(f"User Bet: {user_bet} turtle ")

bots = (bot1, bot2, bot3, bot4, bot5)

if user_bet:
    race_on = True


while race_on:
    for bot in bots:
        bot.speed(random.randint(0, 10))
        bot.fd(random.randint(0, 10))
        if bot.xcor() > 490:
            winner = bot.fillcolor()
            race_on = False

user_bet = user_bet.lower()
winner = winner.lower()

if user_bet == winner:
    print(f"You won!! {winner} turtle won the race")
else:
    print(f"You lost {winner} turtle won the race")

screen.exitonclick()
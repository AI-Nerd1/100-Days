#!/usr/bun/env python3
import turtle
import random
from turtle import Turtle, Screen

screen = Screen()
screen.title("SNAKE GAME")
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
snake = Turtle()


screen.listen()
screen.exitonclick()
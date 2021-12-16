#!/usr/bun/env python3
import turtle
import random
import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.title("SNAKE GAME")
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)

    snake.move()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    

    
    
        




screen.exitonclick()

#!/usr/bun/env python3
import turtle
import random
import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food

screen = Screen()
screen.title("SNAKE GAME")
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)

    snake.move()
    if snake.head.distance(food) < 15:
        print("Eaten")
        food.refresh()


    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    

    
    
        




screen.exitonclick()

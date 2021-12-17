#!/usr/bun/env python3
import turtle
import random
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from collision import Wall_collision


screen = Screen()
screen.title("SNAKE GAME")
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.ht()
wall_collision = Wall_collision()
wall_collision.clear()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
   
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.score += 1
        food.refresh()
        scoreboard.clear()
        scoreboard.current_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        wall_collision.game_over()
    for segment in snake.segments: 
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            wall_collision.game_over()


    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    

    
    
        




screen.exitonclick()

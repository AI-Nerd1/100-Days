from turtle import Turtle
import random
direction = [0,45, 90, 135, 180, 225, 270, 315]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len = 0.6, stretch_wid = 0.6)  
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
        colors = ["darkblue", "DarkOrange","LawnGreen", "MediumVioletRed",
"Salmon", "DeepSkyBlue", "Red", "Yellow", "green",
"orange", "indigo","Blue"]     
        self.color(random.choice(colors))
        self.setheading(random.randint(0,360))
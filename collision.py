from turtle import Turtle

class Wall_collision(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.ht()
        self.game_over()


    def game_over(self):
        self.pu()
        self.goto(0, 0)
        self.write(f"GAME OVER",move=False, align='center', font = ("courier", 24,"normal"))




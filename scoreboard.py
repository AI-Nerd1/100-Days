from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.current_score()
        

    def current_score(self):
        self.pu()
        self.goto(0,260)
        self.write(f"Score: {self.score}",move=False, align='center', font = ("courier", 12,"normal"))



from turtle import Turtle
ALIGNMENT = "Center"
FONT = "Courier"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.cpu_score = 0
        self.update_score()


    def update_score(self):
        self.goto(-100, 200)
        self.write(self.cpu_score, align=ALIGNMENT, font=(FONT, 80, "normal"))
        self.goto(100, 200)
        self.write(self.user_score, align=ALIGNMENT, font=(FONT, 80, "normal"))
    
        
    def add_score(self):
        self.clear()
        self.user_score += 1
        self.update_score()

    def add_score_c(self):
        self.clear()
        self.cpu_score += 1
        self.update_score()
        
from turtle import Turtle, onclick

class CpuPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(-450, 0)

    def Up(self):
        new_y =self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def Down(self):
        new_yy =self.ycor() - 20
        self.goto(self.xcor(), new_yy)
        


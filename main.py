from turtle import Turtle, Screen
from scoreboard import Scoreboard
from cpu_paddle import CpuPaddle
import time
from ball import Ball


screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

turt = Turtle("square")
turt.shapesize(stretch_wid=5, stretch_len=1)
turt.color("white")
turt.penup()
turt.goto(450, 0)

cpu = CpuPaddle()
ball = Ball()
scoreboard = Scoreboard()

def Up():
    new_y =turt.ycor() + 20
    turt.goto(turt.xcor(), new_y)

def Down():
    new_yy =turt.ycor() - 20
    turt.goto(turt.xcor(), new_yy)

screen.listen()
screen.onkey(Up, "Up")
screen.onkey(Down, "Down")
screen.onkey(cpu.Up, "w")
screen.onkey(cpu.Down, "s")

start_game = True
while start_game:
    screen.update()
    time.sleep(ball.movement)
    ball.move()
    
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()
    
    if ball.xcor() > 345 and ball.distance(turt) < 50 or ball.xcor() < -345 and ball.distance(cpu) < 50:
        ball.paddle_collision()
        ball.move()

    if ball.xcor() > 500:
        ball.refresh()
        scoreboard.add_score_c()
  
    if ball.xcor() < -500:
        ball.refresh()
        scoreboard.add_score()
        
















screen.exitonclick()
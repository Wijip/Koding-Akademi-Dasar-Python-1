import time
import turtle
from turtle import *

speed(2)
move_distance = 20

bgcolor("#ffeb86")

penup()
goto(100, 300)
pendown()
color('blue')

begin_fill()
goto(400, 300)
goto(400, -300)
goto(100, -300)
goto(100, 300)
end_fill()

penup()
goto(-200, 0)
shape('turtle')
shapesize(2)
color('green')

def move_up():
    setheading(90)
    forward(move_distance)

def move_down():
    setheading(270)
    forward(move_distance)

def move_left():
    setheading(180)
    forward(move_distance)

def move_right():
    setheading(0)
    forward(move_distance)

def check_goal():
    if xcor() > 100:
        hideturtle()
        color('white')
        write('YOU WIN')

onkey(None, "Up")
onkey(None, "Down")
onkey(None, "Left")
onkey(None, "Right")

onkey(move_up(), "Up")
onkey(move_down(), "Down")
onkey(move_left(), "Left")
onkey(move_right(), "Right")
listen()


time.sleep(10)
turtle.exitonclick()

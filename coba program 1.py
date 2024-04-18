import turtle

win = turtle.Screen()
win.title("Turtle Game")
win.bgcolor("white")

turtle.speed(1)
turtle.shape('turtle')
turtle.color('green')

ocean = turtle.Turtle()
ocean.speed(0)
ocean.shape('square')
ocean.color('blue')
ocean.shapesize(stretch_wid=5, stretch_len=15)
ocean.penup()
ocean.goto(0, -150)

def move_up():
    y = turtle.ycor()
    turtle.tiltangle(90)
    if y < 360:
        turtle.sety(y + 20)
    check_goal()

def move_down():
    y = turtle.ycor()
    turtle.tiltangle(-90)
    if y > -360:
        turtle.sety(y - 20)
    check_goal()

def move_right():
    x = turtle.xcor()
    turtle.tiltangle(0)
    if x < 360:
        turtle.setx(x + 20)
    check_goal()

def move_left():
    x = turtle.xcor()
    turtle.tiltangle(180)
    if x >-360:
        turtle.setx(x - 20)
    check_goal()

def check_goal():
    if turtle.distance(ocean) < 20:
        turtle.penup()
        turtle.color('green')
        ocean.color('blue')
        turtle.goto(0,0)
        turtle.write('You Win!!')

win.listen()
win.onkeypress(move_up, "Up")
win.onkeypress(move_down, "Down")
win.onkeypress(move_right, "Right")
win.onkeypress(move_left, "Left")

win.mainloop()
win.exitonclick()
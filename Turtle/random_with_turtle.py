import turtle
from random import *
from turtle import *

for i in range(10):
    forward(randrange(20,100))
    right(randrange(0,360))
    forward((randrange(20,100)))

turtle.exitonclick()
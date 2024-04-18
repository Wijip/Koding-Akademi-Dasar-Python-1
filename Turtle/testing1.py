import turtle

dodekangon = turtle.Turtle()
turtle.shape(name='turtle')


panjang_sisi = 100

for x in range(12):
    dodekangon.forward(panjang_sisi)
    dodekangon.right(30)




turtle.penup()
turtle.goto(360, 120)
turtle.pendown()

turtle.forward(40)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(100)
turtle.goto(360,20)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(200)



turtle.exitonclick()
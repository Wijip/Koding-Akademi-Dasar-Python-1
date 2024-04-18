import turtle

dodekangon = turtle.Turtle()

panjang_sisi = 100

for x in range(12):
    dodekangon.forward(panjang_sisi)
    dodekangon.right(30)

turtle.exitonclick()

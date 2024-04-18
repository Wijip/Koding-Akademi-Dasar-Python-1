import time
import turtle
import random

t = turtle.Turtle()
s = turtle.screensize(1900,800)

colors = ["red", "blue", "green", "purple", "orange", "pink", "yellow"]
# colors = ["red, blue, green, purple, orange, pink, yellow"]
time.sleep(5)

def bangun_datar():
    warna = random.choice(colors)
    t.fillcolor(warna)
    t.begin_fill()

    jumlah_sisi = random.randint(3,12)

    panjang_sisi= random.randint(50,150)

    for i in range(jumlah_sisi):
        t.forward(panjang_sisi)
        t.left(360 / jumlah_sisi)

    t.end_fill()


random_number = random.randrange(5,20)

for i in range(random_number):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    bangun_datar()

turtle.exitonclick()

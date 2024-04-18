# from random import *
#
# for i in range(5):
#     random_number = randrange(1,10)
#     print(random_number)


import random
import turtle

# Inisialisasi objek Turtle
turtle.Turtle()

turtle.forward(random.randrange(20, 100))
turtle.right(random.randrange(0, 360))
turtle.forward(random.randrange(20, 100))

# Menutup jendela Turtle saat selesai
turtle.done()
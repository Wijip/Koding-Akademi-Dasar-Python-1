import turtle
import time
import random

# Inisialisasi library Turtle dan objek Turtle untuk kedua balapan
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

# Inisialisasi screen
ts = turtle.Screen()
ts.bgcolor("#ffeb86")
ts.title("Turtle Race")


# Fungsi untuk menggambar lintasan untuk Turtle pertama
def draw_track1():
    t1.penup()
    t1.goto(-250, 200)
    t1.pendown()
    t1.color("black")
    t1.pensize(40)
    t1.forward(500)
    t1.penup()


# Fungsi untuk menggambar lintasan untuk Turtle kedua
def draw_track2():
    t2.penup()
    t2.goto(-250, 100)
    t2.pendown()
    t2.color("black")
    t2.pensize(40)
    t2.forward(500)
    t2.penup()


# Fungsi untuk menggambar lintasan untuk Turtle ketiga
def draw_track3():
    t3.penup()
    t3.goto(-250, 0)
    t3.pendown()
    t3.color("black")
    t3.pensize(40)
    t3.forward(500)
    t3.penup()


# Fungsi untuk menggambar lintasan untuk Turtle keempat
def draw_track4():
    t4.penup()
    t4.goto(-250, -100)
    t4.pendown()
    t4.color("black")
    t4.pensize(40)
    t4.forward(500)
    t4.penup()


# Fungsi untuk menggambar lintasan untuk Turtle kelima
def draw_track5():
    t5.penup()
    t5.goto(-250, -200)
    t5.pendown()
    t5.color("black")
    t5.pensize(40)
    t5.forward(500)
    t5.penup()


# Fungsi untuk menampilkan pesan kemenangan dengan posisi yang dapat diatur
def show_winner_message(t, x, y, nama):
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("blue")
    t.write(
        f"SELAMAT {nama} KAMU MENANG",
        align="center",
        font=("Arial", 15, "normal"),
    )


# Membuat lintasan untuk masing-masing Turtle
draw_track1()
draw_track2()
draw_track3()
draw_track4()
draw_track5()

# Membuat Turtle pertama
t1.penup()
t1.goto(-250, 200)
t1.shape("turtle")
t1.color("green")

# Membuat Turtle kedua
t2.penup()
t2.goto(-250, 100)
t2.shape("turtle")
t2.color("red")

# Membuat Turtle ketiga
t3.penup()
t3.goto(-250, 0)
t3.shape("turtle")
t3.color("yellow")

# Membuat Turtle keempat
t4.penup()
t4.goto(-250, -100)
t4.shape("turtle")
t4.color("yellow")

# Membuat Turtle kelima
t5.penup()
t5.goto(-250, -200)
t5.shape("turtle")
t5.color("yellow")

# Kecepatan bergerak untuk masing-masing Turtle
speed_turtle1 = random.randint(1, 5)  # Kecepatan Turtle pertama (1 hingga 5)
speed_turtle2 = random.randint(1, 5)  # Kecepatan Turtle kedua (1 hingga 5)
speed_turtle3 = random.randint(1, 5)  # Kecepatan Turtle ketiga (1 hingga 5)
speed_turtle4 = random.randint(1, 5)  # Kecepatan Turtle keempat (1 hingga 5)
speed_turtle5 = random.randint(1, 5)  # Kecepatan Turtle keempat (1 hingga 5)

# Loop untuk pergerakan kedua Turtle
while True:
    t1.forward(speed_turtle1)
    t2.forward(speed_turtle2)
    t3.forward(speed_turtle3)
    t4.forward(speed_turtle4)
    t5.forward(speed_turtle5)

    # Memeriksa apakah satu dari Turtle mencapai tujuan
    if t1.xcor() >= 230:
        show_winner_message(t1, 0, 200, "T1")  # Turtle pertama mencapai x = 230
        break
    elif t2.xcor() >= 230:
        show_winner_message(t2, 0, 100, "T2")  # Turtle kedua mencapai x = 230
        break
    elif t3.xcor() >= 230:
        show_winner_message(t3, 0, 0, "T3")  # Turtle ketiga mencapai x = 230
        break
    elif t4.xcor() >= 230:
        show_winner_message(t4, 0, -100, "T4")  # Turtle keempat mencapai x = 230
        break
    elif t5.xcor() >= 230:
        show_winner_message(t5, 0, -200, "T5")  # Turtle keempat mencapai x = 230
        break

# Menutup jendela Turtle saat selesai
ts.mainloop()

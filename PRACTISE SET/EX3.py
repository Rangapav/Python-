from turtle import *

speed(2)
bgcolor("red")
penup()
pencolor("blue")
circle(35,60)
right(50)
left(45)
shape("triangle")
right(60)
left(56)
penup()
goto(45,100)

for i in range(3):
    penup()
    goto(36 + i * 15, 156)
    seth(-90)
    pendown()
    pensize(5)
    fd(15 - 2 * i)
    a = -60
    b = 70
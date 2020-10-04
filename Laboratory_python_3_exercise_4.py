import turtle
from random import randint
turtle.hideturtle()
turtle.speed(10)
turtle.penup()
turtle.goto(-300, -300)
turtle.pendown()
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
vx = 10
vy = 10
a = []
dt = 0.1
b = []

number_of_turtles = 1
steps_of_time_number = 10000


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(100)
    unit.goto(randint(-200, 200), randint(-200, 200))
    x, y = unit.position()
    a.append(x)
    a.append(y)
    b.append(vx)
    b.append(vy)
for i in range(steps_of_time_number):
    j = 0
    for unit in pool:
        a[j] += b[j]*dt
        a[j+1] += b[j+1]*dt
        unit.goto(a[j], a[j+1])
        if a[j] < -300 or a[j] > 300:
            b[j] *= -1
        if a[j+1] < -300 or a[j+1] > 300:
            b[j+1] *= -1
        j += 2

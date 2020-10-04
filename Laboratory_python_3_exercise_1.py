import turtle
import random
turtle.shape('turtle')
turtle.color('red')
turtle.speed(100)
for i in range(1000):
    turtle.forward(random.randint(0, 30))
    x = random.randint(0, 1)
    if x == 1:
        turtle.left(random.randint(0, 180))
    else:
        turtle.right(random.randint(0, 180))


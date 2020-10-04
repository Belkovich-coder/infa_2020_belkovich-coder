import turtle
turtle.shape('circle')
turtle.forward(1000)
turtle.penup()
turtle.backward(1000)
turtle.pendown()
turtle.speed(100)
x = 0
y = 0
vx = 1
vy = 20
dt = 0.2
g = 0.5
for i in range(10000):
    turtle.goto(x,y)
    x += vx*dt
    y += vy*dt
    vy -= g*dt
    if y <= 0:
        vy *= -0.9
  
    

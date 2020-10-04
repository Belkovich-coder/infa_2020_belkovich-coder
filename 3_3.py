import turtle as tr
import math

tr.shape('turtle')
tr.speed(10)
tr.left(90)

c = ('tr.forward(20)', 'tr.forward(40)', 'tr.forward(20*math.sqrt(2))',
     'tr.right(45) ', 'tr.right(90)', 'tr.left(45)', 'tr.left(90)',
     'tr.penup()', 'tr.pendown()')


instr = open("turtle_index.txt", 'r').readlines()


def draw_number(num):
    x, y = tr.pos()

    for j in range(len(eval(instr[num]))):
        eval(eval(instr[num])[j])

    tr.penup()
    tr.goto(x + 28, y)
    tr.pendown()


N = list(str(input('Введите число: ', )))
for i in range(len(N)):
    draw_number(int(N[i]))


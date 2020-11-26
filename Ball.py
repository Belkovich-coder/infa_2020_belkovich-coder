import pygame
from pygame.draw import *
import math
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

ochki = [0]

'''этот блок отвечает за появление шариков'''
number = 5
x = []
y = []
r = []
v = []
vx = []
vy = []
alpha = []
typ = []
TYPE = ['CIRCLE', 'SQUARE']
colors = []
for i in range(number):
    x.append(randint(80, 920))
    y.append(randint(80, 820))
    r.append(randint(20, 40))
    v.append(randint(10, 50))
    alpha.append(randint(-180, 180))
    alpha[i] = math.radians(alpha[i])
    vx.append(int(v[i]*math.cos(alpha[i])))
    vy.append(int(v[i]*math.sin(alpha[i])))
    typ.append(TYPE[randint(0, 1)])
    if typ[i] == 'CIRCLE':
        colors.append(COLORS[randint(0, 5)])
        circle(screen, colors[i], (x[i], y[i]), r[i])
    if typ[i] == 'SQUARE':
        colors.append(COLORS[randint(0, 5)])
        rect(screen, colors[i], (x[i], y[i], r[i], r[i]))

def move(j):
    '''отвечает за движение шариков'''
    if typ[j] == 'CIRCLE':
        if x[j] >= 1000 - r[j] or x[j] <= r[j]:
            vx[j] *= -1
            circle(screen, BLACK, (x[j], y[j]), r[j])
            x[j] += vx[j]
            y[j] += vy[j]
            circle(screen, colors[j], (x[j], y[j]), r[j])
        if y[j] >= 900 - r[j] or y[j] <= r[j]:
            vy[j] *= -1
            circle(screen, BLACK, (x[j], y[j]), r[j])
            x[j] += vx[j]
            y[j] += vy[j]
            circle(screen, colors[j], (x[j], y[j]), r[j])
        else:
            circle(screen, BLACK, (x[j], y[j]), r[j])
            x[j] += vx[j]
            y[j] += vy[j]
            circle(screen, colors[j], (x[j], y[j]), r[j])
    if typ[j] == 'SQUARE':
        if x[j] >= 1000 - r[j] or x[j] <= r[j]:
            vx[j] *= -1
            rect(screen, BLACK, (x[j], y[j], r[j], r[j]))
            x[j] += vx[j]
            y[j] += vy[j]
            rect(screen, colors[j], (x[j], y[j], r[j], r[j]))
        if y[j] >= 900 - r[j] or y[j] <= r[j]:
            vy[j] *= -1
            rect(screen, BLACK, (x[j], y[j], r[j], r[j]))
            x[j] += vx[j]
            y[j] += vy[j]
            rect(screen, colors[j], (x[j], y[j], r[j], r[j]))
        else:
            rect(screen, BLACK, (x[j], y[j], r[j], r[j]))
            x[j] += vx[j]
            y[j] += vy[j]
            rect(screen, colors[j], (x[j], y[j], r[j], r[j]))


def click(event, k):
    '''проверяет попадание мышкой по шарику и ведет подсчет очков'''
    global points, coord
    coord = event.pos
    if pow((coord[0]-x[k])**2+(coord[1]-y[k])**2, 0.5) <= r[k]:
        print('Hit!')
        if typ[k] == 'CIRCLE':
            points += 1
        if typ[k] == 'SQUARE':
            points += 5

def score(points):
    '''отображает количество очков на игровом поле'''
    rect(screen, BLACK, (0, 0, 300, 40))
    my_font = pygame.font.Font(None, 50)
    string = "Очки: " + str(points)
    text = my_font.render(string, 1, RED)
    screen.blit(text, (3, 3))

def revival(k):
    '''создает новый шарик'''
    if typ[k] == 'CIRCLE':
        circle(screen, BLACK, (x[k], y[k]), r[k])
    if typ[k] == 'SQUARE':
        rect(screen, BLACK, (x[k], y[k], r[k], r[k]))
    x[k] = randint(80, 920)
    y[k] = randint(80, 820)
    r[k] = randint(20, 40)
    v[k] = randint(10, 50)
    alpha[k] = randint(-180, 180)
    alpha[k] = math.radians(alpha[k])
    vx.append(int(v[k]*math.cos(alpha[k])))
    vy.append(int(v[k]*math.sin(alpha[k])))
    typ[k] = TYPE[randint(0, 1)]
    if typ[k] == 'CIRCLE':
        colors[k] = COLORS[randint(0, 5)]
        circle(screen, colors[k], (x[k], y[k]), r[k])
    if typ[k] == 'SQUARE':
        colors[k] = COLORS[randint(0, 5)]
        rect(screen, colors[k], (x[k], y[k], r[k], r[k]))
    
            
pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0


save_results = False
file = open('result.txt','a')
name = ''

def print_comment(comment, x, y, size):
    font = pygame.font.Font(None, size)
    text = font.render(comment, True, RED)
    screen.blit(text, [x, y])

def save_scores(final_score, name):
    if name == '':
        name = 'Player'
    file.write(name + " : " + str(final_score) + '\n')





while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_results = True
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            for t in range(number):
                click(event, t)
                if pow((coord[0]-x[t])**2+(coord[1]-y[t])**2, 0.5) <= r[t]:
                    score(points)
                    revival(t)
            
    for u in range(number):
        move(u)
    pygame.display.update()

while save_results:
    screen.fill(BLACK)
    clock.tick(FPS)
    print_comment("Enter your name:", 400, 300, 60)
    print_comment("Use only small letters and numbers, please", 350, 350, 30)
    print_comment("Press 'Enter' to save your result", 400, 500, 30)
    print_comment(name, 400, 400, 72)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_results = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                save_results = False
            elif (event.key < 123 and event.key > 96) or (event.key < 58 and event.key > 47):
                name += chr(event.key)
    pygame.display.update()

save_scores(points, name)
file.close()

pygame.quit()

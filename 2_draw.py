import pygame
from pygame.draw import *
from math import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))
screen.fill([220, 220, 220])
rect(screen, [0, 255, 255], (0, 0, 600, 400))
rect(screen, [47, 79, 79], (-5, -5, 610, 405), 2)

ellipse(screen, [220, 220, 220], (0, 300, 200, 300))
ellipse(screen, [0, 0, 0], (0, 300, 200, 300), 2)
#sun
circle(screen, [240, 255, 255], (450, 150), 125, 10)
circle(screen, [224, 255, 255], (450, 150), 10)
circle(screen, [224, 255, 255], (325, 150), 10)
circle(screen, [224, 255, 255], (575, 150), 10)
circle(screen, [224, 255, 255], (450, 25), 10)
circle(screen, [224, 255, 255], (450, 275), 10)
rect(screen, [224, 255, 255], (315, 140, 250, 20))
rect(screen, [224, 255, 255], (440, 15, 20, 250))

#YDOChKA
arc(screen, [0, 0, 0], (190, 200, 500, 500), pi/2, pi, 3)

ellipse(screen, [220, 220, 220], (170, 380, 70, 40))
ellipse(screen, [0, 0, 0], (170, 380, 70, 40), 2)

ellipse(screen, [220, 220, 220], (100, 520, 130, 90))
ellipse(screen, [0, 0, 0], (100, 520, 130, 90), 2)

ellipse(screen, [220, 220, 220], (190, 580, 90, 40))
ellipse(screen, [0, 0, 0], (190, 580, 90, 40), 2)

#head
ellipse(screen, [220, 220, 220], (100, 250, 100, 70))
ellipse(screen, [0, 0, 0], (100, 250, 100, 70), 2)

line(screen, [0, 0, 0], (130, 300), (190, 300))

circle(screen, [0, 0, 0], (150, 280), 5)

circle(screen, [0, 0, 0], (200, 290), 5)

circle(screen, [220, 220, 220], (110, 260), 10)
circle(screen, [0, 0, 0], (110, 260), 10, 1)

ellipse(screen, [128, 128, 128], (370, 500, 180, 100))
ellipse(screen, [0, 0, 0], (370, 500, 180, 100), 1)
ellipse(screen, [85, 107, 47], (380, 530, 160, 70))
ellipse(screen, [0, 0, 0], (380, 530, 160, 70), 1)

line(screen, [0, 0, 0], (440, 200), (450, 550))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

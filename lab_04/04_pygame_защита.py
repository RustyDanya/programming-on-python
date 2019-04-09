# Воробьев Даниил ИУ7-21Б

import pygame
from math import *

# Создание окна
window = pygame.display.set_mode((900, 500))
screen = pygame.Surface((900, 500))
road = pygame.Surface((900, 100))
pygame.display.set_caption("4 laba")

# Цвета
sky = (135, 206, 235)
green = (0, 77, 0)
black = (0,0,0)
grey = (192, 192, 192)
blue = (0, 0, 255)
brown = (102, 53, 0)
yellow = (255, 255, 0)

# Переменные для движения автобуса
wheel1_x = -100
wheel1_y = 382
wheel1_change =  2
angle = 3.14
angle1 = 1.57
x = wheel1_x - 10
y = wheel1_y
x1 = wheel1_x
y1 = wheel1_y - 10
time = 0


run = True
while run:
    # Проверка на выход из программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(sky)
    road.fill(brown)

    # Изменение позиции колес
    x = wheel1_x + 10*cos(angle)
    y = wheel1_y + 10*sin(angle)
    x1 = wheel1_x + 10*cos(angle1)
    y1 = wheel1_y + 10*sin(angle1)
    angle+=0.095
    angle1+=0.095
    
    # Танк   
    pygame.draw.line(screen, black, ( wheel1_x + 40, 340), (wheel1_x + 40, 300), 2)
    pygame.draw.line(screen, blue, ( wheel1_x + 39, 301), (wheel1_x + 28, 301), 4)
    pygame.draw.line(screen, yellow, ( wheel1_x + 39, 305), (wheel1_x + 28, 305), 4)
    pygame.draw.line(screen, green, ( wheel1_x + 40, 340), (wheel1_x + 150, 340), 10)
    pygame.draw.circle(screen, green, (wheel1_x + 40, 365), 40)
    pygame.draw.ellipse(screen, green, (wheel1_x - 40, 360, 165, 45))
    pygame.draw.ellipse(screen, black, (wheel1_x - 40, 360, 165, 45), 6)
    


    
    # Колеса    
    pygame.draw.circle(screen, black, (int(wheel1_x), wheel1_y), 15)
    pygame.draw.circle(screen, black, (int(wheel1_x) + 90, wheel1_y), 15)
    pygame.draw.circle(screen, grey, (int(wheel1_x), wheel1_y), 11, 2)
    pygame.draw.circle(screen, grey, (int(wheel1_x) + 90, wheel1_y), 11, 2)
    
    pygame.draw.line(screen, grey, (x,y),
                     (2*wheel1_x - x, 2 * wheel1_y - y), 1)
    pygame.draw.line(screen, grey, (x1,y1),
                     (2*wheel1_x - x1, 2 * wheel1_y - y1), 1)

    pygame.draw.line(screen, grey, (x+90,y),
                     (2*wheel1_x - x+90, 2 * wheel1_y - y), 1)
    pygame.draw.line(screen, grey, (x1+90,y1),
                     (2*wheel1_x - x1+90, 2 * wheel1_y - y1), 1)
    





    # Смещение
    wheel1_x += wheel1_change

    # Зацикливание    
    if wheel1_x == 900:
        time += 1
    if time > 0 and time < 100:
        time += 1
    if time >= 100:
        wheel1_x = -300
        time = 0


    window.blit(screen, (0, 0))
    window.blit(road, (0,400))
    pygame.display.flip()
    pygame.time.delay(20)
pygame.quit()

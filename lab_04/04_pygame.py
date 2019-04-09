# Воробьев Даниил ИУ7-21Б

import pygame
from math import *

# Создание окна
window = pygame.display.set_mode((900, 500))
screen = pygame.Surface((900, 500))
road = pygame.Surface((900, 100))
pygame.display.set_caption("4 laba")

# Цвета
asphalt = (90,90,90)
sky = (135, 206, 235)
red = (255, 0, 0)
green = (34, 139, 34)
black = (0,0,0)
grey = (192, 192, 192)
man = (255, 127, 80)
white = (255, 255, 255)
blue = (0, 0, 255)
brown = (102, 53, 0)

# Переменные для движения автобуса
wheel1_x = -2000
wheel1_y = 385
wheel1_change = 5
angle = 3.14
angle1 = 1.57
x = wheel1_x - 10
y = wheel1_y
x1 = wheel1_x
y1 = wheel1_y - 10

# Переменные для движения человека
pas_x = 1000
pas_y = 380
pas_change = 1
foot = 2
i = 0
time = 0
time2 = 0

run = True
while run:
    # Проверка на выход из программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(sky)
    road.fill(asphalt)

    # Изменение позиции колес
    if wheel1_x < 540 or time > 100:
        x = wheel1_x + 10*cos(angle)
        y = wheel1_y + 10*sin(angle)
        x1 = wheel1_x + 10*cos(angle1)
        y1 = wheel1_y + 10*sin(angle1)
        angle+=0.095
        angle1+=0.095

    # Рисование облаков
    pygame.draw.rect(screen, white, [280,90,60,40])
    pygame.draw.circle(screen, white,[280,110],20 )
    pygame.draw.circle(screen, white, [340,105],25)
    pygame.draw.circle(screen, white, [300,90],17)
    pygame.draw.circle(screen, white, [325,80],20)
    pygame.draw.rect(screen, white, [640,110,60,40])
    pygame.draw.circle(screen, white,[640,130],20 )
    pygame.draw.circle(screen, white, [700,125],25)
    pygame.draw.circle(screen, white, [660,110],17)
    pygame.draw.circle(screen, white, [685,100],20)

    # Остановка
    pygame.draw.rect(screen, black, (550, 335 , 100, 75), 6)
    pygame.draw.rect(screen, green, (553, 338 , 94, 63))
    pygame.draw.rect(screen, white, (670, 338 , 20, 10))
    pygame.draw.rect(screen, black, (667, 338 , 23, 13),6)
    pygame.draw.line(screen, black, (677, 348), (677, 400), 6)

    # Пассажир идет на остановку
    if foot % 64 == 0:
        i = 3
    else:
        if foot % 32 == 0:
            i = 0
            
    if time < 100:
        # Пассажир идет на остановку
        pygame.draw.line(screen, blue, (int(pas_x), int(pas_y)), (pas_x + 5 - i, pas_y + 20), 3)
        pygame.draw.line(screen, blue, (pas_x, pas_y), (pas_x - 5 + i, pas_y + 20), 3)
        pygame.draw.line(screen, brown, (pas_x, pas_y), (pas_x, pas_y - 20), 3)
        pygame.draw.line(screen, brown, (pas_x, pas_y - 20), (pas_x + 5, pas_y), 3)
        pygame.draw.line(screen, brown, (pas_x, pas_y - 20), (pas_x - 5, pas_y), 3)
        pygame.draw.circle(screen, man, (int(pas_x), 352), 8)
        pygame.draw.circle(screen, black, (int(pas_x) - 5, 352), 1)
        pygame.draw.line(screen, red, (pas_x - 2, 356), (pas_x - 4, 356), 1)
    else:
        # Пассажир в автобусе
        pygame.draw.circle(screen, man, (int(wheel1_x) + 60, 340), 8)
        pygame.draw.circle(screen, black, (int(wheel1_x) + 60 - 5, 340), 1)
        pygame.draw.line(screen, red, (wheel1_x + 60 - 2, 344), (wheel1_x + 60 - 4, 344), 1)
        pygame.draw.line(screen, brown, (wheel1_x + 60, pas_y - 20), (wheel1_x + 60, pas_y - 33), 3)
        pygame.draw.line(screen, brown, (wheel1_x + 60 - 10, 355), (wheel1_x + 60, 348), 4)

    # Водитель автобуса
    pygame.draw.circle(screen, man, (int(wheel1_x) + 112, 340), 8)
    pygame.draw.circle(screen, black, (int(wheel1_x) + 117, 340), 1)
    pygame.draw.line(screen, red, (wheel1_x+115, 344), (wheel1_x+117,344), 1)
    pygame.draw.line(screen, blue, (wheel1_x+112, 348), (wheel1_x+122,355), 3)
    pygame.draw.line(screen, blue, (wheel1_x+112, 348), (wheel1_x+112,355), 4)

    # Автобус
    pygame.draw.rect(screen, red, (wheel1_x - 30, 355 , 163, 40))
    pygame.draw.rect(screen, red, (wheel1_x - 29, 325 , 65, 30), 4)
    pygame.draw.rect(screen, red, (wheel1_x + 35, 325 , 66, 30), 4)
    pygame.draw.rect(screen, red, (wheel1_x + 100, 325 , 31, 30), 4)

    # Колеса    
    pygame.draw.circle(screen, black, (int(wheel1_x), wheel1_y), 15)
    pygame.draw.circle(screen, black, (int(wheel1_x) + 105, wheel1_y), 15)
    pygame.draw.circle(screen, grey, (int(wheel1_x), wheel1_y), 11, 2)
    pygame.draw.circle(screen, grey, (int(wheel1_x) + 105, wheel1_y), 11, 2)
    
    pygame.draw.line(screen, grey, (x,y),
                     (2*wheel1_x - x, 2 * wheel1_y - y), 1)
    pygame.draw.line(screen, grey, (x1,y1),
                     (2*wheel1_x - x1, 2 * wheel1_y - y1), 1)

    pygame.draw.line(screen, grey, (x+105,y),
                     (2*wheel1_x - x+105, 2 * wheel1_y - y), 1)
    pygame.draw.line(screen, grey, (x1+105,y1),
                     (2*wheel1_x - x1+105, 2 * wheel1_y - y1), 1)

    # Смещение автобуса
    if wheel1_x < 540 or time > 100:
        wheel1_x += wheel1_change
    else:
        time += 2
        
    # Смещение пассажира    
    if pas_x > 600: 
        pas_x -= pas_change
        foot += 1

    # Зацикливание    
    if wheel1_x == 900:
        time2 += 1
    if time2 > 0 and time2 < 100:
        time2 += 1
    if time2 >= 100:
        wheel1_x = -2000
        pas_x = 1000
        time = 0
        time2 = 0
        foot = 2
        i = 0

    window.blit(screen, (0, 0))
    window.blit(road, (0,400))
    pygame.display.flip()
    pygame.time.delay(10)
pygame.quit()

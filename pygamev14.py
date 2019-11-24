# -*- coding: UTF-8 -*-
import pygame
import time
import random
pygame.init()
win = pygame.display.set_mode((3300,1900))
pygame.display.set_caption("hralyb best game")
x = 0
y = 0
widht = 100
height = 100
x2 = 2900
y2 = 1800
widht2 = 100
height2 = 100
vel = 100
vel2 = 100
bust = 0
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
boosts = 0
speedbonus = 0
speedbonus2 = 0
invybonus = 1000000000000
invybonus2 = 100000000000
telebonus = 0
telebonus2 = 0
shbonus = 0
shbonus2 = 0
massbonus = 0
massbonus2 = 0
sizebonus = 0
sizebonus2 = 0
shield = 0
shield2 = 0
COLOR = BLUE
COLOR2 = GREEN
COLORT = BLUE
COLORT2 = GREEN
COLORB11 = (0, 0, 0)
COLORB21 = (0, 0, 0)
COLORB12 = (0, 0, 0)
COLORB22 = (0, 0, 0)
COLORB13 = (0, 0, 0)
COLORB23 = (0, 0, 0)
COLORB14 = (0, 0, 0)
COLORB24 = (0, 0, 0)
COLORB15 = (0, 0, 0)
COLORB25 = (0, 0, 0)
boosti = 0
boostk = 0
boostt = 0
boostsh = 0
boostsz = 0
COLORINVY = BLUE
COLORINVY2 = GREEN
xinvy = 5000
yinvy = 5000
xspeed = 5000
yspeed = 5000
xtele = 5000
ytele = 5000
xshield = 5000
xsize = 5000
ysize = 5000
catch = 100
catch2 = 100
yshield = 5000
point = 0
point2 = 0
wino = 0
wino2 = 0
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = false
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_j]:
        x -= vel
    if keys[pygame.K_l]:
        x += vel
    if keys[pygame.K_i]:
        y -= vel
    if keys[pygame.K_k]:
        y += vel
    if keys[pygame.K_SPACE]:
        widht += vel
        height += vel
    if COLORT == BLUE and COLORT2 == GREEN:
        if(x < 100 or x > 2800):
            x = 100
        if(y < 100 or y > 1700):
            y = 100
        if(x2 < 100 or x2 > 2800):
            x2 = 2700
        if(y2 < 100 or y2 > 1700):
            y2 = 1600
    if COLORT == BLUE and COLORT2 == BLUE:
        if(x < 100):
            x = 2800
        if(x > 2800):
            x = 100
        if(y < 100):
            y = 1700
        if(y > 1700):
            y = 100
        if(x2 < 100):
            x2 = 200
        if(x2 > 2800):
            x2 = 2700
        if(y2 < 100):
            y2 = 200
        if(y2 > 1700):
            y2 = 1600
    if COLORT == GREEN and COLORT2 == GREEN:
        if(x2 < 100):
            x2 = 2800
        if(x2 > 2800):
            x2 = 100
        if(y2 < 100):
            y2 = 1700
        if(y2 > 1700):
            y2 = 100
        if(x < 100):
            x = 200
        if(x > 2800):
            x = 2700
        if(y < 100):
            y = 200
        if(y> 1700):
            y = 1600
    if keys[pygame.K_BACKSPACE]:
        widht -= vel
        height -= vel
    if keys[pygame.K_q]:
        x2 = 2900
        y2 = 1800
    if keys[pygame.K_a]:
        x2 -= vel2
    if keys[pygame.K_d]:
        x2 += vel2
    if keys[pygame.K_w]:
        y2 -= vel2
    if keys[pygame.K_s]:
        y2 += vel2
    if keys[pygame.K_LSHIFT]:
        widht2 += vel2
        height2 += vel2
    if keys[pygame.K_TAB]:
        widht2 -= vel2
        height2 -= vel2
    if widht >= 1000:
        widht = 10
        height = 10
    if widht <= 0:
        widht = 100
        height = 100
    if widht2 >= 1000:
        widht2 = 10
        height2 = 10
    if widht2 <= 0:
        widht2 = 100
        height2 = 100
    if keys[pygame.K_r]:
        x = 0
        y = 0
        x2 = 2800
        y2 = 1700
        widht = 100
        height = 100
        widht2 = 100
        height2 = 100
        starttime = time.monotonic()
    if COLORINVY == BLUE and (x >= x2-catch and x <= x2 + catch) and (y >= y2-catch and y <= y2+catch) and shield2 == 0:
        COLORINVY = RED
        COLORINVY2 = BLUE
        x = 100
        y = 100
        x2 = 2800
        y2 = 1700
        vel = 100
        vel2 = 100
        endtime = time.monotonic()
        catchtime = endtime - starttime
        print("za", catchtime, "sekund modrý chytil zeleného")
        point2 = point2 + catchtime
        starttime = time.monotonic()
    if COLORINVY2 == BLUE and (x2 >= x-catch2 and x2 <= x + catch2) and (y2 >= y-catch2 and y2 <= y+catch2) and shield == 0:
        COLORINVY2 = GREEN
        COLORINVY = BLUE
        x = 100
        y = 100
        x2 = 2800
        y2 = 1700
        vel = 100
        vel2 = 100
        endtime = time.monotonic()
        catchtime = endtime - starttime
        print("za", catchtime, "sekund zelený chytil modrého")
        point = point + catchtime
        starttime = time.monotonic()
    boostkk = time.monotonic()
    if boostkk - boostk >= 10:
        bust = random.randint(1,5)
        print(bust)
    if boosts == 0 and bust == 1:
        xspeed = random.randint(1,28)
        yspeed = random.randint(1,17)
        boosts = 1
        boostk = time.monotonic()
        bust = 0
    if boosti == 0 and bust == 2:
        xinvy = random.randint(1,28)
        yinvy = random.randint(1,17)
        boosti = 1
        boostk = time.monotonic()
        bust = 0
    if boostt == 0 and bust == 3:
        xtele = random.randint(1,28)
        ytele = random.randint(1,17)
        boostt = 1
        boostk = time.monotonic()
        bust = 0
    if boostsh == 0 and bust == 4:
        xshield = random.randint(1,28)
        yshield = random.randint(1,17)
        boostsh = 1
        boostk = time.monotonic()
        bust = 0
    if boostsz == 0 and bust == 5:
        xsize = random.randint(1,28)
        ysize = random.randint(1,17)
        boostsz = 1
        boostk = time.monotonic()
        bust = 0
    if x == xinvy * 100 and y == yinvy * 100:
        COLOR = (0, 0, 0)
        boosti = 0
        xinvy = 5000
        yinvy = 5000
        invybonus = time.monotonic()
        COLORB12 = (255, 255, 255)
    if x2 == xinvy * 100 and y2 == yinvy * 100:
        boosti = 0
        xinvy = 5000
        yinvy = 5000
        invybonus2 = time.monotonic()
        COLOR2 = (0, 0, 0)
        COLORB22 = (255, 255, 255)
    if x == xsize * 100 and y == ysize * 100:
        catch = 200
        xsize = 5000
        boostsz = 0
        sizebonus = time.monotonic()
        COLORB15 = (255, 171, 0)
    if x2 == xsize * 100 and y2 == ysize * 100:
        catch2 = 200
        xsize = 5000
        boostsz = 0
        sizebonus2 = time.monotonic()
        COLORB25 = (255, 171, 0)
    if x == xspeed * 100 and y == yspeed * 100:
        vel = 200
        xspeed = 5000
        boosts = 0
        speedbonus = time.monotonic()
        COLORB11 = (0, 255, 255)
    if x2 == xspeed * 100 and y2 == yspeed * 100:
        vel2 = 200
        xspeed = 5000
        boosts = 0
        speedbonus2 = time.monotonic()
        COLORB21 = (0, 255, 255)
    if x == xshield * 100 and y == yshield * 100:
        shield = 1
        xshield = 5000
        boostsh = 0
        shbonus = time.monotonic()
        COLORB14 = (255, 0, 255)
    if x2 == xshield * 100 and y2 == yshield * 100:
        shield2 = 1
        xshield = 5000
        boostsh = 0
        shbonus2 = time.monotonic()
        COLORB24 = (255, 0, 255)
    teleminus = time.monotonic()
    teleminus2 = time.monotonic()
    shminus = time.monotonic()
    shminus2 = time.monotonic()
    if teleminus - telebonus >= 10:
        COLORT2 = GREEN
        COLORB13 = (0, 0, 0)
    if teleminus2 - telebonus2 >= 10:
        COLORT = BLUE
        COLORB23 = (0, 0, 0)
    if shminus - shbonus >= 5:
        shield = 0
        COLORB14 = (0, 0, 0)
    if shminus2 - shbonus2 >= 5:
        shield2 = 0
        COLORB24 = (0, 0, 0)
    if x == xtele * 100 and y == ytele * 100:
        boostt = 0
        telebonus = time.monotonic()
        COLORT = BLUE
        COLORT2 = BLUE
        xtele = 5000
        COLORB13 = (255, 255, 0)
    if x2 == xtele * 100 and y2 == ytele * 100:
        boostt = 0
        COLORT = GREEN
        COLORT2 = GREEN
        telebonus2 = time.monotonic()
        xtele = 5000
        COLORB23 = (255, 255, 0)
    speedbonusminus = time.monotonic()
    speedbonusminus2 = time.monotonic()
    invybonusminus = time.monotonic()
    invybonusminus2 = time.monotonic()
    sizebonusminus = time.monotonic()
    sizebonusminus2 = time.monotonic()
    if invybonusminus - invybonus >= 3:
        COLOR = BLUE
        COLORB12 = (0, 0, 0)
    if invybonusminus2 - invybonus2 >= 3:
        COLOR2 = GREEN
        COLORB22 = (0, 0, 0)
    if speedbonusminus - speedbonus >= 5:
        vel = 100
        COLORB11 = (0, 0, 0)
    if speedbonusminus2 - speedbonus2 >= 5:
        vel2 = 100
        COLORB21 = (0, 0, 0)
    if sizebonusminus - sizebonus >= 5:
        catch = 100
        COLORB15 = (0, 0, 0)
    if sizebonusminus2 - sizebonus2 >= 5:
        catch2 = 100
        COLORB25 = (0, 0, 0)
    if point >= 38:
        print("PLAYER ONE (BLUE) WIN")
        point = 0
        point2 = 0
        wino = wino + 100
    if point2 >= 38:
        print("PLAYER TWO (GREEN) WIN")
        point = 0
        point2 = 0
        wino2 = wino2 + 100
    win.fill((0))
    if COLORINVY == BLUE:
        pygame.draw.circle(win, COLOR, [x+50, y+50], 50)
        pygame.draw.rect(win, COLOR2, (x2, y2, widht2, height2))
    if COLORINVY2 == BLUE:
        pygame.draw.circle(win, COLOR2, [x2+50, y2+50], 50)       
        pygame.draw.rect(win, COLOR, (x, y, widht, height))
    
    pygame.draw.rect(win, COLORT2, (0, 0, 3000, 100))       
    pygame.draw.rect(win, COLORT, (0, 1800, 3000, 100))
    pygame.draw.rect(win, COLORT, (2900, 0, 100, 1800))       
    pygame.draw.rect(win, COLORT2, (0, 0, 100, 1800))
    pygame.draw.rect(win, (0, 255, 255), (xspeed * 100, yspeed * 100, 100,100))
    pygame.draw.rect(win, (255, 255, 255), (xinvy * 100, yinvy * 100, 100,100))
    pygame.draw.rect(win, (255, 255, 0), (xtele * 100, ytele * 100, 100,100))
    pygame.draw.rect(win, (255, 0, 255), (xshield * 100, yshield * 100, 100,100))
    pygame.draw.rect(win, (255, 171, 0), (xsize * 100, ysize * 100, 100,100))
    pygame.draw.rect(win, BLUE, (3010, 0, 40, point * 50))
    pygame.draw.rect(win, GREEN, (3060, 0, 40, point2 * 50))
    pygame.draw.rect(win, RED, (3010, 0, 40, wino))
    pygame.draw.rect(win, RED, (3060, 0, 40, wino2))
    pygame.draw.rect(win, BLUE,(3110, 0, 90, 90))
    pygame.draw.rect(win, GREEN,(3210, 0, 90, 90))
    pygame.draw.rect(win, COLORB11,(3110, 100, 90, 90))
    pygame.draw.rect(win, COLORB12,(3110, 200, 90, 90))
    pygame.draw.rect(win, COLORB13,(3110, 300, 90, 90))
    pygame.draw.rect(win, COLORB14,(3110, 400, 90, 90))
    pygame.draw.rect(win, COLORB15,(3110, 500, 90, 90))
    pygame.draw.rect(win, COLORB21,(3210, 100, 90, 90))
    pygame.draw.rect(win, COLORB22,(3210, 200, 90, 90))
    pygame.draw.rect(win, COLORB23,(3210, 300, 90, 90))
    pygame.draw.rect(win, COLORB24,(3210, 400, 90, 90))
    pygame.draw.rect(win, COLORB25,(3210, 500, 90, 90))
    pygame.display.update()

pygame.quit()
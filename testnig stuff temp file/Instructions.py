
import math, random
import pygame
from pygame.locals import *
from settings import *
from functions import *

screen.fill(sBackground)
help1 = font2.render("Instructions", True, BLACK)

help2 = font5.render("The goal of this game is simple, get to the top.", True, BLACK)
help3 = font5.render("To move use W to go left, D to go right, and the space bar to jump.", True, BLACK)
help4 = font5.render("The player can hop from platform to platform simply by coming in contact with it.", True, BLACK)
help5 = font5.render("Once you reach the highest platform jump above the top of the screen to proceed to the next section.", True, BLACK)
help6 = font5.render("After you have proceeded to the second sections your handi-cap will be disabled.", True, BLACK)
help7 = font5.render("Now if you fall off of all of the platforms and end up at the bottom of the screen, you lose.", True, BLACK)
help8 = font5.render("Enjoy!", True, BLACK)


screen.blit(help1, (200, 40))
screen.blit(help2, (240, 320))
screen.blit(help3, (160, 350))
screen.blit(help4, (100, 380))
screen.blit(help5, (5, 410))
screen.blit(help6, (100, 440))
screen.blit(help7, (75, 470))
screen.blit(help8, (420, 500))

running = True
while running:
    pygame.event.pump()
    k = pygame.key.get_pressed()
    if k[pygame.K_q] or k[pygame.K_ESCAPE]:
        break
    x,y = pygame.mouse.get_pos()

    pygame.draw.circle(screen, sMainButtonClr2, (50, h - 50), RAD2)
    pygame.draw.circle(screen, BLACK, (50, h - 50), RAD2, 10)
    line4 = font4.render("Back", True, BLACK)
    screen.blit(line4, (20, h - 65))

    if checkInCir(50, h- 50, y, x, RAD2):
        sMainButtonClr2 = sButtonClrPressed
        if pygame.mouse.get_pressed()[0]:
            helpStart = True
    else:
        sMainButtonClr2 = sButtonClr

    pygame.display.flip()
pygame.quit()
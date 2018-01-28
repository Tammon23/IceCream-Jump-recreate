import math, random
import pygame
from pygame.locals import *
from settings import *
from functions import *

lossScreen = True
while lossScreen:
    pygame.event.pump()
    k = pygame.key.get_pressed()
    if k[pygame.K_q] or k[pygame.K_ESCAPE]:
        break

    #start Splash screen
    screen.fill(sBackground)
    line1 = font2.render("You Lose!", True, BLACK)
    line2 = font5.render("Your final score was: " + str(points), True, BLACK)
    screen.blit(line1, (90, 100))
    screen.blit(line2, (90, 210))

    line3 = font1.render("- By Ikenna Uduh", True, BLACK)
    screen.blit(line3, (w - 150, h - 25))

    x,y = pygame.mouse.get_pos()

    pygame.draw.circle(screen, sPAgainButtonClr, (int(w/2), int(h/2 + 50)), RAD3)
    pygame.draw.circle(screen, BLACK, (int(w/2), int(h/2 + 50)), RAD3, 10)
    line3 = font3.render("PLAY", True, BLACK)
    line4 = font3.render("AGAIN", True, BLACK)
    screen.blit(line3, (int(w/2) - 120, 400))
    screen.blit(line4, (int(w/2) - 120, 500))


    # Checking to see if the clicked mouse is pressing the PLAY or HELP buttons
    if checkInCir(int(w/2), int(h/2 + 50), y, x, RAD3):
        sPAgainButtonClr = sButtonClrPressed
        if pygame.mouse.get_pressed()[0]:
            gameStart = True
    else:
        sPAgainButtonClr = sButtonClr


    pygame.display.flip()
pygame.quit()


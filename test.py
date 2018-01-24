import math, random
import pygame
from pygame.locals import *
from settings import *
from functions import *

running = True
while running:
    pygame.event.pump()
    k = pygame.key.get_pressed()
    if k[pygame.K_q] or k[pygame.K_ESCAPE]:
        break

    #start Splash screen
    screen.fill(sBackground)
    line1 = font2.render("IceCream Jump", True, BLACK)
    screen.blit(line1, (90, 100))

    line2 = font1.render("- By Ikenna Uduh", True, BLACK)
    screen.blit(line2, (w - 150, h - 25))

    x,y = pygame.mouse.get_pos()

    pygame.draw.circle(screen, sMainButtonClr, (int(w/2), 450), RAD)
    pygame.draw.circle(screen, BLACK, (int(w/2), 450), RAD, 10)
    line3 = font3.render("PLAY", True, BLACK)
    screen.blit(line3, (int(w/2) - 99, 400))

    pygame.draw.circle(screen, sMainButtonClr2, (50, h - 50), RAD2)
    pygame.draw.circle(screen, BLACK, (50, h - 50), RAD2, 10)
    line4 = font4.render("HELP!", True, BLACK)
    screen.blit(line4, (15, h - 65))

    # Checking to see if the clicked mouse is pressing the PLAY or HELP buttons
    if checkInCir(int(w/2), 450, y, x, RAD):
        sMainButtonClr = sButtonClrPressed
        if pygame.mouse.get_pressed()[0]:
            gameStart = True
    else:
        sMainButtonClr = sButtonClr

    if checkInCir(50, h- 50, y, x, RAD2):
        sMainButtonClr2 = sButtonClrPressed
        if pygame.mouse.get_pressed()[0]:
            helpStart = True
            screen.fill(sBackground)

            screen.blit(help1, (200, 40))
            screen.blit(help2, (240, 320))
            screen.blit(help3, (160, 350))
            screen.blit(help4, (100, 380))
            screen.blit(help5, (5, 410))
            screen.blit(help6, (100, 440))
            screen.blit(help7, (75, 470))
            screen.blit(help8, (420, 500))
            while helpStart:
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
                        helpStart = False
                else:
                    sMainButtonClr2 = sButtonClr

                pygame.display.flip()

    else:
        sMainButtonClr2 = sButtonClr


    pygame.display.flip()
pygame.quit()



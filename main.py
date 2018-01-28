#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     To create a game for my cs FSE
#
# Author:      Ikenna Uduh, 35300999
#
# Created:     15-12-2017
#-------------------------------------------------------------------------------


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
               # #####################################################################  Game logic
            # ### creating the list  of values holding all of the platform's x and y location data
            initialPlatform = gen_start_platforms(150, platSize,size, 80)
            #print("Number of platforms seen:",len(initialPlatform), initialPlatform )

            pygame.mixer.music.play(-1)
            # Let's start the game
            while gameStart:
                pygame.event.pump()
                k = pygame.key.get_pressed()
                if k[pygame.K_q] or k[pygame.K_ESCAPE]:
                    break
                #pygame.mixer.music.play(-1)

                ## Calculating the points, based on movements
                if trackY > yPos:
                    points += trackY - yPos
                    trackY = yPos

                ##Blitting images to to the screen
                # Blit'n the points in the top left corner
                screen.blit(bgimg, (0,0))

                for platform in initialPlatform:
                    screen.blit(platformPic, (platform))

                if startFloor:
                    screen.blit(scale_floorImg, (0, h - platSize[1]))

                screen.blit(player, (xPos,yPos-playerSize[1]))

                pointTxt = font1.render("Total Score:"+ str(points), True, BLACK)
                screen.blit(pointTxt, (0, 0))

                stageTxt = font1.render("Stage:"+ str(stage), True, BLACK)
                screen.blit(stageTxt, (int(w/2), 0))


                ##Checking to see if certain keys are pressed and preforming tasks if so
                if k[K_a]: xPos -= xVel; player = playerL
                elif k[K_d]: xPos += xVel; player = playerR
                if k[pygame.K_SPACE] and onGround:
                    jumpping = True
                    onGround = False


                ##Implimenting jumpping
                if jumpping:
                    player = playerU
                    yPos -= yVel
                    jumpCounter += 1


                # if player is jumoping then wait until they reach their max jump height
                if jumpCounter == maxJumpHeight:
                    jumpping = False
                    jumpCounter = 0

                ## Implimenting Gravity

                #if (not onGround or not onPlat) and not jumpping:
                if not onGround and not jumpping:
                    if not startFloor:
                        yPos += gravVel
                    elif startFloor:
                        if yPos <= (h - platform[1] + 20):
                            yPos += gravVel


                ## if the players goes off to the left or right screen they get moved to the opposing side
                if xPos + playerSize[0] <= 0:
                    xPos = w - 1

                if xPos >= w:
                    xPos = -playerSize[0]

                ## if the player goes off of the top of the screen then generate a new map, and move the player to the bottom of the screen
                if yPos <= 0:
                    yPos = h
                    startFloor = False
                    jumpCounter = 0
                    initialPlatform = gen_start_platforms(0, platSize,size, 80, (xPos, h-platSize[1]))
                    trackY = h# - platSize[1] + 20
                    stage += 1
                    enemyVel = int(stage/2)
                    enemyX = 0
                    enemyY = random.randint(0, int(h/2))

                # Adding enemies in to spice some things up
                if stage > 1:
                    addEnemy(screen, enemyX, enemyY, scale_enemy ,(xPos, yPos-playerSize[1], playerSize[0], playerSize[1]))
                    if addEnemy(screen, enemyX, enemyY, scale_enemy ,(xPos, yPos-playerSize[1], playerSize[0], playerSize[1])):
                        pygame.mixer.music.stop()
                        pygame.mixer.Sound.play(crash_sound)
                        lossScreen = True
                        gameStart = False

                    if enemyX <= 0:
                        enemyX = 1
                        enemyVel *= -1
                        scale_enemy = pygame.transform.flip(scale_enemy,True,False)

                    elif enemyX + enemySize[0] >= w:
                        enemyX = w - enemySize[0] - 1
                        enemyVel *= -1
                        scale_enemy = pygame.transform.flip(scale_enemy,True,False)

                    enemyX += enemyVel

                ## Detecing if the player is on top of a platform
                for platform in initialPlatform:
                    # ### detecting if the player is on the platform
                    if detectCollisions(h, xPos, yPos, playerSize[0], platform[0], platform[1], platSize[0], platSize[1], gravVel, startFloor):
                        if not jumpping:
                            yPos = platform[1]
                            onGround = True
                            break


                    elif yPos >= (h - platSize[1] + 20) and startFloor:
                        yPos = h - platSize[1] + 20
                        onGround = True


                    elif yPos >= h and trackY < h-platSize[1]:# if the players falls through the bottom of the screen, if so they lose :D
                        lossScreen = True
                        gameStart = False

                    elif not jumpping :
                            onGround = False

                pygame.display.flip()
                CLOCK.tick(FPS)


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

    #if the player lost display the loss screen
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
                lossScreen = False
                # Reseting all starting parameters
                scale_enemy = pygame.transform.flip(pygame.transform.scale(enemy, (platSize)),True,False)
                player = playerU
                xPos = int(w/2)
                yPos = h - platSize[1] + 20
                onGround = True
                jumpping = False
                startFloor = True
                trackY = yPos
                stage = 1
                points = 0
                enemyVel = 1
                pygame.mixer.music.unpause()
        else:
            sPAgainButtonClr = sButtonClr


        pygame.display.flip()
    pygame.display.flip()
pygame.quit()
import math, random
import pygame
from pygame.locals import *
from settings import *

#Generating the intial amount of platforms that will be appended into a list
def gen_start_platforms(startPlatY, platSize, screenSize, platformGap):
    platformLoc = []
    imgWidth = platSize[0]
    for i in range(screenSize[1]-startPlatY, 0, -platformGap):
        x = (random.randint(0, screenSize[0]- imgWidth),i)
        platformLoc.append(x)
    return platformLoc


def detectCollisions(h, x1,y1,w1,x2,y2,w2,h2, yVel, startFloor):
    global onFloor
    global onGround
    if startFloor and y1 <= h - h2 + 20 and y1 + yVel >= h - h2 + 20:
        onFloor = True
        #onGround = True
        print("floor")
        return True

    elif (x2 <= x1 <= x2 + w2 and y1 <= y2 and y1 + yVel >= y2):
        print("left half")
        #onGround = True
        return True

    elif (x2 <= x1 + w1 <= x2 + w2 and y1 <= y2 and y1 + yVel >= y2):
        print("right half")
        #onGround = True
        return True

    else:
        #onGround = True
        onFloor = False
        return False

def movePlatform(listOfPlat, platSize, index):
    global platMoveValue

    if (listOfPlat[index][0] == w - platSize[0]) or (listOfPlat[index][0] == 0):
        platMoveValue *= -1

    listOfPlat[index][0] += platMoveValue

# ### creating the list  of values holding all of the platform's x and y location data
initialPlatform = gen_start_platforms(150, platSize,size, 80)
print("Number of platforms seen:",len(initialPlatform), initialPlatform )


# Let's start the game
while True:
    pygame.event.pump()
    k = pygame.key.get_pressed()
    if k[pygame.K_q] or k[pygame.K_ESCAPE]:
        break

    ## Calculating the points, based on movements
    if trackY > yPos:
        points += abs(trackY - yPos)
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

    print("Gavity on false: ", onGround, "false:", jumpping)
    ## Implimenting Gravity
    if not onGround and not jumpping:
        yPos += gravVel

    ## if the players goes off to the left or right screen they get moved to the opposing side
    if xPos + playerSize[0] <= 0:
        xPos = w - 1

    if xPos >= w:
        xPos = 0 - playerSize[0]

    ## if the player goes off of the top of the screen then generate a new map, and move the player to the bottom of the screen
    if yPos <= 0:
        yPos = h
        startFloor = False
        initialPlatform = gen_start_platforms(0, platSize,size, 80)
        trackY = h - platSize[1] + 20


    ## Detecing if the player is on top of a platform
    for platform in initialPlatform:
        if detectCollisions(h, xPos, yPos, playerSize[0], platform[0], platform[1], platSize[0], platSize[1], gravVel, startFloor):# x1,y1,w1,x2,y2,w2, yVel
##            if yPos <= h - platSize[1] + 20 and yPos + gravVel:
##                yPos = h - platSize[1] + 20
            if onFloor and not jumpping:
                yPos = h - platSize[1] + 20
            #if  platform[1] >= yPos and platform[1] <= yPos + yVel:
            else:
                yPos = platform[1]
            onGround = True
        else: pass
             #onGround = False
    pygame.display.flip()

    if yPos > h and not startFloor:
##        screen.fill(WHITE)
##        pygame.display.flip()
##        pygame.time.wait(500)
##        screen.fill(RED)
##        pygame.display.flip()
##        pygame.time.wait(400)
##        screen.fill(WHITE)
##        pygame.display.flip()
##        pygame.time.wait(300)
##        for i in range(6):
##            screen.fill(RED)
##            pygame.display.flip()
##            pygame.time.wait(200)
##            screen.fill(WHITE)
##            pygame.display.flip()
##            pygame.time.wait(200)
##
##        pointTxt = font2.render("YOU LOSE!", True, BLACK)
##        screen.blit(pointTxt, (0, int(h/2)))
##        pygame.display.flip()
##        pygame.time.wait(3000)


        break


    CLOCK.tick(FPS)
pygame.quit()

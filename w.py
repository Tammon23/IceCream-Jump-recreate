import math, random
import pygame
from pygame.locals import *

# define display surface
size = w, h = 900, 880

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ice Cream Magnet Jump")
FPS = 120

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)


# Pictures used in program
platformPic = pygame.image.load("Singleplatform.png")
playerR = pygame.image.load("playerLRight.png")
playerL = pygame.image.load("playerLLeft.png")
playerD = pygame.image.load("playerLDead.png")
playerU = pygame.image.load("playerLJump.png")


# ### getting sizes of each picture drawn
platSize = platformPic.get_rect().size
playerSize = player.get_rect().size

points = 0
trackY = h
font1 = pygame.font.SysFont("arial",20)


#Movement varibles
maxJumpHeight = 60

xPos = 100#int(w/2)
yPos = h #- playerSize[1]
gravVel = 1
yVel = 4
xVel = 1
jumpCounter = 0
onGround = True
onPlatform = True
jumpping = False
gravTEST = 0

#Generating the intial amount of platforms that will be appended into a list
def gen_start_platforms(imageSize, screenSize, platformGap):
    platformLoc = []
    imgWidth = imageSize[0]
    for i in range(platformGap, screenSize[1], platformGap):
        x = (random.randint(0, screenSize[0]- imgWidth),i)
        platformLoc.append(x)
    return platformLoc

##def platformMove(coords, yspeed):
##    print("start", coords)
##    for coord in coords:
##        print("ok")
##        coord = (coord[0], coord[1] - yspeed)
##    return coords
##    print("end", coords)

# ### creating the list  of values holding all of the platform's x and y location data
initialPlatform = gen_start_platforms(platSize,size, 80)
print("Number of platforms seen:",len(initialPlatform) )

# Let's start the game
def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):
    if (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):

        return True

    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):

        return True

    else:

        return False

class Game:

    def __init__(self,x,y,width,height):

        self.x=x

        self.y=y

        self.width=width

        self.height=height

    def rendee(self,collision):

        if (collision==True):pass


    def moveX(self, x):
        self.x += x

    def moveY(self, y):
        self.y += y




while True:
    pygame.event.pump()
    k = pygame.key.get_pressed()
    if k[pygame.K_q] or k[pygame.K_ESCAPE]:
        break
    screen.fill(WHITE)

    # ## Dectecting if the space is pressed, therefore jumpping
    if k[pygame.K_SPACE] and onGround == True:
        jumpping = True
        onGround = False


    if jumpping == True:
        print("ok")
        player = playerU
        yPos -= yVel
        jumpCounter += 1
        onPlatform = False
        # ifplayer is jumoping then wait until they reach their max jump height
        if jumpCounter == maxJumpHeight:
            jumpping = False
            jumpCounter = 0


    # Blit'n the points in the top left corner
    pointTxt = font1.render("Total Score:"+ str(points), True, BLACK)
    screen.blit(pointTxt, (0, 0))


    # Gravity
    if onGround == False and jumpping == False:
        yPos += gravVel
        gravTEST += 1
        print("ok2")

    # if the players goes off to the left or right screen they get moved to the opposing side
    if xPos <= 0:
        xPos = w - 1
    if xPos >= w:
        xPos = 0

    # if the player is on the beginning floor then...
    if yPos >= h:
        yPos = h
        onGround = True
    # if the player goes off of the top of the screen then generate a new map, and move the player to the bottom of the screen
    if yPos <= 0:
        yPos = h
        initialPlatform = gen_start_platforms(platSize,size, 80)
        trackY = h

    # ##Adding in points based on movements
    if trackY <= h:
        if trackY > yPos:
            points += abs(trackY - yPos)
            trackY = yPos

##    if onGround == True and jumpping == True:   ##########################################################
##        jumpping = False

##    # if the player's y value is half way on the screen then move all platforms downward
##    if yPos <= int(h/2):
##        test = 0
##        print(initialPlatform, "ko")
##        for coord in initialPlatform:
##            initialPlatform[test] = (coord[0], coord[1] + yVel)
##            test += 1
##        print(initialPlatform, "ok2")
##        #initialPlatform = platformMove(initialPlatform, yVel)
##        #print("adjusdted", initialPlatform)



    if k[K_a]: xPos -= xVel; player = playerL
    elif k[K_d]: xPos += xVel; player = playerR

    #Blit n each platform onto the screen to their repective coords
    for platform in initialPlatform:
        # ### detecting if the player is on the platform
        #if platform[0] <= xPos <= platform[0] + platSize[0] and yPos <= platform[1] and yPos + yVel >= platform[1]:
        if detectCollisions(platform[0], platform[1], platSize[0], platSize[1], xPos, yPos, playerSize[0], playerSize[1]):# x1,y1,w1,h1,x2,y2,w2,h2
            if yPos != platform[1]:
                yPos = platform[1]
                onGround = True
                onPlatform = True
                #jumpCounter = 0




        #pygame.draw.rect(screen, RED, (platform[0], platform[1], platSize[0], platSize[1]))
        screen.blit(platformPic, (platform))#drawing the platforms



    pygame.draw.circle(screen, (0, 255, 0), (xPos, yPos), 5)
    screen.blit(player, (xPos,yPos-playerSize[1]))

    pygame.display.flip()
    CLOCK.tick(FPS)
    #print("Jumpping:", jumpping, "on the ground:", onGround, "Gravity counter:", gravTEST, "Jump counter:", jumpCounter)
pygame.quit()
import pygame
from pygame.locals import *
# define display surface
size = w, h = 900, 880

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ice Cream Magnet Jump")
FPS = 300

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)

#Splash screen Colours
sBackground = 97, 232, 196
sButtonClr = 239, 148, 29
sButtonClrPressed = 230, 201, 163
sMainButtonClr = sButtonClr
sMainButtonClr2 = sButtonClr

# Pictures used in program
platformPic = pygame.image.load("Singleplatform.png").convert_alpha()
playerR = pygame.image.load("playerLRight.png").convert_alpha()
playerL = pygame.image.load("playerLLeft.png").convert_alpha()
playerD = pygame.image.load("playerLDead.png").convert_alpha()
playerU = pygame.image.load("playerLJump.png").convert_alpha()
floorImg = pygame.image.load("floor.png").convert_alpha()
bgimg = pygame.image.load("bg.jpg").convert_alpha()
player = playerU



# ### getting sizes of each picture drawn
platSize = platformPic.get_rect().size
playerSize = player.get_rect().size

#Scaling the image down to something we can use
scale_floorImg = pygame.transform.scale(floorImg, (w, platSize[1]))

points = 0
trackY = h
font1 = pygame.font.SysFont("arial",20)
font2 = pygame.font.SysFont("arial",100)
font3 = pygame.font.SysFont("arial",80)
font4 = pygame.font.SysFont("arial",25)
font5 = pygame.font.SysFont("arial",20)

#Movement varibles
maxJumpHeight = 60

#Words of wisdom
help1 = font2.render("Instructions", True, BLACK)

help2 = font5.render("The goal of this game is simple, get to the top.", True, BLACK)
help3 = font5.render("To move use W to go left, D to go right, and the space bar to jump.", True, BLACK)
help4 = font5.render("The player can hop from platform to platform simply by coming in contact with it.", True, BLACK)
help5 = font5.render("Once you reach the highest platform jump above the top of the screen to proceed to the next section.", True, BLACK)
help6 = font5.render("After you have proceeded to the second sections your handi-cap will be disabled.", True, BLACK)
help7 = font5.render("Now if you fall off of all of the platforms and end up at the bottom of the screen, you lose.", True, BLACK)
help8 = font5.render("Enjoy!", True, BLACK)




xPos = 100#int(w/2)
yPos = h - platSize[1] + 20
gravVel = 1
yVel = 1
xVel = 2
jumpCounter = 0
onGround = True
onPlatform = True
jumpping = False
gravTEST = 0
startFloor = True
index = 0
trackY = yPos

onFloor = False #Vaule showing if the player is on the grass starting floor

platMoveValue = 1
RAD = 125
RAD2 = 50

gameStart = False
helpStart = False
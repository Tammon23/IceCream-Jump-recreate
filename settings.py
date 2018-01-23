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


#Movement varibles
maxJumpHeight = 60

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
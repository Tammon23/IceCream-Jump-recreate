#-------------------------------------------------------------------------------
# Name:        settings.py
# Purpose:     To create a game for my cs FSE
#
# Author:      Ikenna Uduh, 35300999
#
# Created:     15-12-2017
#-------------------------------------------------------------------------------


import pygame
from pygame.locals import *
# define display surface
size = w, h = 900, 880

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ice Cream Magnet Jump")
FPS =  300

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
sPAgainButtonClr = sButtonClr

# Pictures used in program
unscaled_platformPic = pygame.image.load("imgs/Singleplatform.png").convert_alpha()
platformPic = pygame.transform.scale(unscaled_platformPic, (100, 51))
enemy = pygame.image.load("imgs/enemy.png").convert_alpha()
playerR = pygame.image.load("imgs/playerLRight.png").convert_alpha()
playerL = pygame.image.load("imgs/playerLLeft.png").convert_alpha()
playerD = pygame.image.load("imgs/playerLDead.png").convert_alpha()
playerU = pygame.image.load("imgs/playerLJump.png").convert_alpha()
floorImg = pygame.image.load("imgs/floor.png").convert_alpha()
bgimg = pygame.image.load("imgs/bg.jpg").convert_alpha()
player = playerU

# ### getting sizes of each picture drawn
platSize = platformPic.get_rect().size

#Scaling the image down to something we can use
scale_floorImg = pygame.transform.scale(floorImg, (w, platSize[1]))
scale_enemy = pygame.transform.flip(pygame.transform.scale(enemy, (platSize)),True,False)

# ### getting sizes pictures drawn
playerSize = player.get_rect().size
enemySize = scale_enemy.get_rect().size



# loading in fonts
font1 = pygame.font.SysFont("arial",20)
font2 = pygame.font.SysFont("arial",100)
font3 = pygame.font.SysFont("arial",80)
font4 = pygame.font.SysFont("arial",25)
font5 = pygame.font.SysFont("arial",50)


#Words of wisdom
help1 = font2.render("Instructions", True, BLACK)

help2 = font1.render("The goal of this game is simple, get to the top.", True, BLACK)
help3 = font1.render("To move use W to go left, D to go right, and the space bar to jump.", True, BLACK)
help4 = font1.render("The player can hop from platform to platform simply by coming in contact with it.", True, BLACK)
help5 = font1.render("Once you reach the highest platform jump above the top of the screen to proceed to the next section.", True, BLACK)
help6 = font1.render("After you have proceeded to the second sections your handi-cap will be disabled.", True, BLACK)
help7 = font1.render("Now if you fall off of all of the platforms and end up at the bottom of the screen, you lose.", True, BLACK)
help8 = font1.render("Enjoy!", True, BLACK)


#Sounds
bg_music = pygame.mixer.music.load("sounds/bg_music.mp3")
walk_sound = pygame.mixer.Sound('sounds/walk_sound.mp3')
crash_sound = pygame.mixer.Sound('sounds/Crash.mp3')

#Movement varibles
maxJumpHeight = 220

xPos = int(w/2)             # players x location
yPos = h - platSize[1] + 20 # players y location
gravVel = 1
yVel = 1 # movement speed along the vertical axis
xVel = 2 # movement speed along the horizontal axis
jumpCounter = 0
onGround = True  # if the player is on a platform
jumpping = False # if the player is preforming a jump
startFloor = True # defining if there should be a starting platform at the start of the stage
trackY = yPos # used in determining amount of points

points = 0
stage = 1
RAD = 125 # radius of the play button
RAD2 = 50 # radius of the help button
RAD3 = 200 # radius of the play again button

enemyX = 1 # The enemy's starting location in pixels
enemyVel = 1 # The enemy's starting velocity

lossScreen = False # if  the losing/play again screen is shown
gameStart = False  # if the actual game is running or not
helpStart = False  # if the help screen is being shown
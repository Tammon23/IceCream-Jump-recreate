#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     To create a game for my cs FSE
#
# Author:      Ikenna Uduh, 35300999
#
# Created:     15-12-2017
#-------------------------------------------------------------------------------


import random

#Generating the intial amount of platforms that will be appended into a list
def gen_start_platforms(startPlatY, platSize, screenSize, platformGap, addPlat1=False):
    platformLoc = []
    t = screenSize[1]-startPlatY
    if addPlat1 != False:
        platformLoc.append(addPlat1)

    imgWidth = platSize[0]
    for i in range(screenSize[1]-startPlatY, 0, -platformGap):
        x = (random.randint(0, screenSize[0]- imgWidth),t)
        platformLoc.append(x)
        t -= platformGap
    return platformLoc


def detectCollisions(h, x1,y1,w1,x2,y2,w2,h2, yVel, startFloor):
    if (x2 <= x1 <= x2 + w2 and y1 <= y2 and y1 + yVel >= y2):
        return True

    elif (x2 <= x1 + w1 <= x2 + w2 and y1 <= y2 and y1 + yVel >= y2):
        return True

    elif (x2 <= x1 + int(w1/2) <= x2 + w2 and y1 <= y2 and y1 + yVel >= y2):
        return True

    else:
        return False

def movePlatform(listOfPlat, platSize, index):
    global platMoveValue

    if (listOfPlat[index][0] == w - platSize[0]) or (listOfPlat[index][0] == 0):
        platMoveValue *= -1

    listOfPlat[index][0] += platMoveValue
    pygame.display.update(listOfPlat[0], listOfPlat[1], platSize[0], platSize[1])

def checkInCir(x1, y1, a, b, c):
    y = abs(y1 - a)
    x = abs(x1 - b)
    if (y**2 + x**2)**0.5 <= c:
        return True
    else:
        return False


def addEnemy(screen, x1, y1, enemyPic, playerPos):
    #~1 enemy ~2player
    screen.blit(enemyPic, (x1, y1))
    w1 = enemyPic.get_rect().size[0]
    h1 = enemyPic.get_rect().size[1]

    x2 = playerPos[0]
    y2 = playerPos[1]
    w2 = playerPos[2]
    h2 = playerPos[3]

    if (x2 + w2 >= x1 >= x2 and y2+h2 >= y1 >= y2):  #bottom left of player
        return True
    elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2): #bottom right
        return True
    elif (x2 + w2 >= x1 >= x2 + w2 and y2 + h2 >=  y1 + h1 >= y2): #top left
        return True
    elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2): #Top right
        return True
    else:
        return False
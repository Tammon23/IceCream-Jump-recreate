import random

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

def checkInCir(x1, y1, a, b, c):
    y = abs(y1 - a)
    x = abs(x1 - b)
    if (y**2 + x**2)**0.5 <= c:
        return True
    else:
        return False



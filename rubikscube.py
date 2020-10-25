from vpython import *
import numpy as np
import time
import random

scene.background = color.white

def createSmallCube(i, color1, color2, color3, color4, color5, color6): #i is the cube's locational number

    cubeLocation = vector((i%3)-1, floor(i/9)-1, floor((i%9)/3)-1)
    
    tinyBox1 = box(pos = cubeLocation + vector(0.25, 0, 0), length = 0.5, width = 0.99, height = 0.99, color = color1) #tinyBox refers to the boxes that make the smallCube
    tinyBox2 = box(pos = cubeLocation - vector(0.25, 0, 0), length = 0.5, width = 0.99, height = 0.99, color = color2)
    tinyBox3 = box(pos = cubeLocation + vector(0, 0.25, 0), length = 0.99, width = 0.99, height = 0.5, color = color3)
    tinyBox4 = box(pos = cubeLocation - vector(0, 0.25, 0), length = 0.99, width = 0.99, height = 0.5, color = color4)
    tinyBox5 = box(pos = cubeLocation + vector(0, 0, 0.25), length = 0.99, width = 0.5, height = 0.99, color = color5)
    tinyBox6 = box(pos = cubeLocation - vector(0, 0, 0.25), length = 0.99, width = 0.5, height = 0.99, color = color6)
    
    cube = compound([tinyBox1, tinyBox2, tinyBox3, tinyBox4, tinyBox5, tinyBox6])
    return cube

#27 small cubes

smallCubeList = []

smallCubeList.append(createSmallCube(0, color.magenta, color.red, color.magenta, color.white, color.magenta, color.blue))
smallCubeList.append(createSmallCube(1, color.magenta, color.magenta, color.magenta, color.white, color.magenta, color.blue))
smallCubeList.append(createSmallCube(2, color.orange, color.magenta, color.magenta, color.white, color.magenta, color.blue))
smallCubeList.append(createSmallCube(3, color.magenta, color.red, color.magenta, color.white, color.magenta, color.red))
smallCubeList.append(createSmallCube(4, color.magenta, color.magenta, color.magenta, color.white, color.magenta, color.magenta)) #bottom middle cube
smallCubeList.append(createSmallCube(5, color.orange, color.magenta, color.magenta, color.white, color.magenta, color.magenta))
smallCubeList.append(createSmallCube(6, color.magenta, color.red, color.magenta, color.white, color.green, color.magenta))
smallCubeList.append(createSmallCube(7, color.magenta, color.magenta, color.magenta, color.white, color.green, color.magenta))
smallCubeList.append(createSmallCube(8, color.orange, color.magenta, color.magenta, color.white, color.green, color.magenta))

smallCubeList.append(createSmallCube(9, color.magenta, color.red, color.magenta, color.magenta, color.magenta, color.blue))
smallCubeList.append(createSmallCube(10, color.magenta, color.magenta, color.magenta, color.magenta, color.magenta, color.blue)) #back middle cube
smallCubeList.append(createSmallCube(11, color.orange, color.red, color.magenta, color.magenta, color.magenta, color.blue))
smallCubeList.append(createSmallCube(12, color.magenta, color.red, color.magenta, color.magenta, color.magenta, color.magenta)) #left middle cube
smallCubeList.append(createSmallCube(13, color.magenta, color.magenta, color.magenta, color.magenta, color.magenta, color.magenta)) #center cube
smallCubeList.append(createSmallCube(14, color.orange, color.magenta, color.magenta, color.magenta, color.magenta, color.magenta)) #right middle cube
smallCubeList.append(createSmallCube(15, color.magenta, color.red, color.magenta, color.magenta, color.green, color.magenta))
smallCubeList.append(createSmallCube(16, color.magenta, color.magenta, color.magenta, color.magenta, color.green, color.magenta)) #front middle cube
smallCubeList.append(createSmallCube(17, color.orange, color.magenta, color.magenta, color.magenta, color.green, color.magenta))

smallCubeList.append(createSmallCube(18, color.magenta, color.red, color.yellow, color.magenta, color.magenta, color.blue))
smallCubeList.append(createSmallCube(19, color.magenta, color.magenta, color.yellow, color.magenta, color.magenta, color.blue))
smallCubeList.append(createSmallCube(20, color.orange, color.magenta, color.yellow, color.magenta, color.magenta, color.blue))
smallCubeList.append(createSmallCube(21, color.magenta, color.red, color.yellow, color.magenta, color.magenta, color.magenta))
smallCubeList.append(createSmallCube(22, color.magenta, color.magenta, color.yellow, color.magenta, color.magenta, color.magenta)) #top middle
smallCubeList.append(createSmallCube(23, color.orange, color.magenta, color.yellow, color.magenta, color.magenta, color.magenta))
smallCubeList.append(createSmallCube(24, color.magenta, color.red, color.yellow, color.magenta, color.green, color.magenta))
smallCubeList.append(createSmallCube(25, color.magenta, color.magenta, color.yellow, color.magenta, color.green, color.magenta))
smallCubeList.append(createSmallCube(26, color.orange, color.magenta, color.yellow, color.magenta, color.green, color.magenta))

#making array that stores colors on cube faces

colors = np.array([[["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]],
                   [["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]],
                   [["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]],
                   [["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]],
                   [["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]],
                   [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]]])

storage = np.copy(colors)


#exit()
#------------------------------------------------------------------- turns -------------------------------------------------------------------

solution = []
stagePause = 0
rotatePause = 0

def isEqual(A, B):
    epsilon = 0.01
    if (abs(A - B) < epsilon):
        return True
    else:
        return False

def rotate(angle, axis, face, value, pause):
    for n in range(0, 90):
        for i in range(0, 27):
            if (face == "x"):
                if (isEqual(smallCubeList[i].pos.x, value)):
                    smallCubeList[i].rotate(angle = angle/90, axis = axis, origin = vector(0, 0, 0))
            if (face == "y"):
                if (isEqual(smallCubeList[i].pos.y, value)):
                    smallCubeList[i].rotate(angle = angle/90, axis = axis, origin = vector(0, 0, 0))
            if (face == "z"):
                if (isEqual(smallCubeList[i].pos.z, value)):
                    smallCubeList[i].rotate(angle = angle/90, axis = axis, origin = vector(0, 0, 0))
        time.sleep(pause)

def r():

    global colors
    global storage
    
    rotate(-pi/2, vector(1, 0, 0), "x", 1, rotatePause)
           
    for i in range(0, 9):
        storage[5, floor(i/3), i%3] = colors[5, 2-(i%3), floor(i/3)]
    
    for i in range(0, 3):
        storage[1, i, 2] = colors[3, i, 2]
        storage[3, i, 2] = colors[0, i, 2]
        storage[0, i, 2] = colors[2, 2-i, 0]
        storage[2, 2-i, 0] = colors[1, i, 2]

    colors = np.copy(storage)
    solution.append("r")
    
def rPrime():

    global colors
    global storage
    
    rotate(pi/2, vector(1, 0, 0), "x", 1, rotatePause)
            
    for i in range(0, 9):
        storage[5, floor(i/3), i%3] = colors[5, i%3, 2-(floor(i/3))]

    for i in range(0, 3):
       storage[1, i, 2] = colors[2, 2-i, 0]
       storage[2, 2-i, 0] = colors[0, i, 2]
       storage[0, i, 2] = colors[3, i, 2]
       storage[3, i, 2] = colors[1, i, 2]

    colors = np.copy(storage)
    solution.append("rPrime")
    
def l():

    global colors
    global storage
    
    rotate(pi/2, vector(1, 0, 0), "x", -1, rotatePause)
            
    for i in range(0, 9):
        storage[4, floor(i/3), i%3] = colors[4, 2-(i%3), floor(i/3)]

    for i in range(0, 3):
       storage[1, i, 0] = colors[2, 2-i, 2]
       storage[2, 2-i, 2] = colors[0, i, 0]
       storage[0, i, 0] = colors[3, i, 0]
       storage[3, i, 0] = colors[1, i, 0]

    colors = np.copy(storage)
    solution.append("l")

def lPrime():

    global colors
    global storage
    
    rotate(-pi/2, vector(1, 0, 0), "x", -1, rotatePause)
            
    for i in range(0, 9):
        storage[4, floor(i/3), i%3] = colors[4, i%3, 2-(floor(i/3))]

    for i in range(0, 3):
       storage[1, i, 0] = colors[3, i, 0]
       storage[3, i, 0] = colors[0, i, 0]
       storage[0, i, 0] = colors[2, 2-i, 2]
       storage[2, 2-i, 2] = colors[1, i, 0]
       
    colors = np.copy(storage)
    solution.append("lPrime")

def u():

    global colors
    global storage
    
    rotate(-pi/2, vector(0, 1, 0), "y", 1, rotatePause)

    for i in range(0, 9):
        storage[1, floor(i/3), i%3] = colors[1, 2-(i%3), floor(i/3)]

    for i in range(0, 3):
       storage[3, 0, i] = colors[5, 0, i]
       storage[5, 0, i] = colors[2, 0, i]
       storage[2, 0, i] = colors[4, 0, i]
       storage[4, 0, i] = colors[3, 0, i]

    colors = np.copy(storage)
    solution.append("u")

def uPrime():

    global colors
    global storage

    rotate(pi/2, vector(0, 1, 0), "y", 1, rotatePause)
            
    for i in range(0, 9):
        storage[1, floor(i/3), i%3] = colors[1, i%3, 2-(floor(i/3))]

    for i in range(0, 3):
       storage[3, 0, i] = colors[4, 0, i]
       storage[4, 0, i] = colors[2, 0, i]
       storage[2, 0, i] = colors[5, 0, i]
       storage[5, 0, i] = colors[3, 0, i]
       
    colors = np.copy(storage)
    solution.append("uPrime")
    
def d():

    global colors
    global storage
    
    rotate(pi/2, vector(0, 1, 0), "y", -1, rotatePause)
            
    for i in range(0, 9):
        storage[0, floor(i/3), i%3] = colors[0, 2-(i%3), floor(i/3)]
    
    for i in range(0, 3):
       storage[3, 2, i] = colors[4, 2, i]
       storage[4, 2, i] = colors[2, 2, i]
       storage[2, 2, i] = colors[5, 2, i]
       storage[5, 2, i] = colors[3, 2, i]
       
    colors = np.copy(storage)
    solution.append("d")

def dPrime():

    global colors
    global storage
    
    rotate(-pi/2, vector(0, 1, 0), "y", -1, rotatePause)
            
    for i in range(0, 9):
        storage[0, floor(i/3), i%3] = colors[0, i%3, 2-(floor(i/3))]
        
    for i in range(0, 3):
       storage[3, 2, i] = colors[5, 2, i]
       storage[5, 2, i] = colors[2, 2, i]
       storage[2, 2, i] = colors[4, 2, i]
       storage[4, 2, i] = colors[3, 2, i]

    colors = np.copy(storage)
    solution.append("dPrime")
    
def f():

    global colors
    global storage
    
    rotate(-pi/2, vector(0, 0, 1), "z", 1, rotatePause)
            
    for i in range(0, 9):
        storage[3, floor(i/3), i%3] = colors[3, 2-(i%3), floor(i/3)]
    
    for i in range(0, 3):
       storage[1, 2, i] = colors[4, 2-i, 2]
       storage[4, 2-i, 2] = colors[0, 0, 2-i]
       storage[0, 0, 2-i] = colors[5, i, 0]
       storage[5, i, 0] = colors[1, 2, i]

    colors = np.copy(storage)
    solution.append("f")

def fPrime():

    global colors
    global storage
    
    rotate(pi/2, vector(0, 0, 1), "z", 1, rotatePause)
    
    for i in range(0, 9):
        storage[3, floor(i/3), i%3] = colors[3, i%3, 2-(floor(i/3))]

    for i in range(0, 3):
       storage[1, 2, i] = colors[5, i, 0]
       storage[5, i, 0] = colors[0, 0, 2-i]
       storage[0, 0, 2-i] = colors[4, 2-i, 2]
       storage[4, 2-i, 2] = colors[1, 2, i]

    colors = np.copy(storage)
    solution.append("fPrime")

def b():

    global colors
    global storage
    
    rotate(pi/2, vector(0, 0, 1), "z", -1, rotatePause)
            
    for i in range(0, 9):
        storage[2, floor(i/3), i%3] = colors[2, 2-(i%3), floor(i/3)]
    
    for i in range(0, 3):
       storage[1, 0, i] = colors[5, i, 2]
       storage[5, i, 2] = colors[0, 2, 2-i]
       storage[0, 2, 2-i] = colors[4, 2-i, 0]
       storage[4, 2-i, 0] = colors[1, 0, i]

    colors = np.copy(storage)
    solution.append("b")

def bPrime():

    global colors
    global storage
    
    rotate(-pi/2, vector(0, 0, 1), "z", -1, rotatePause)
            
    for i in range(0, 9):
        storage[2, floor(i/3), i%3] = colors[2, i%3, 2-(floor(i/3))]

    for i in range(0, 3):
       storage[1, 0, i] = colors[4, 2-i, 0]
       storage[4, 2-i, 0] = colors[0, 2, 2-i]
       storage[0, 2, 2-i] = colors[5, i, 2]
       storage[5, i, 2] = colors[1, 0, i]

    colors = np.copy(storage)
    solution.append("bPrime")

def m():

    global colors
    global storage
    
    rotate(-pi/2, vector(1, 0, 0), "x", 0, rotatePause)

    for i in range(0, 3):
       storage[3, i, 1] = colors[0, i, 1]
       storage[0, i, 1] = colors[2, 2-i, 1]
       storage[2, 2-i, 1] = colors[1, i, 1]
       storage[1, i, 1] = colors[3, i, 1]

    colors = np.copy(storage)
    solution.append("m")

def mPrime():

    global colors
    global storage
    
    rotate(pi/2, vector(1, 0, 0), "x", 0, rotatePause)

    for i in range(0, 3):
       storage[3, i, 1] = colors[1, i, 1]
       storage[1, i, 1] = colors[2, 2-i, 1]
       storage[2, 2-i, 1] = colors[0, i, 1]
       storage[0, i, 1] = colors[3, i, 1]
       
    colors = np.copy(storage)
    solution.append("mPrime")

def e():

    global colors
    global storage
    
    rotate(-pi/2, vector(0, 1, 0), "y", 0, rotatePause)

    for i in range(0, 3):
       storage[3, 1, i] = colors[5, 1, i]
       storage[5, 1, i] = colors[2, 1, i]
       storage[2, 1, i] = colors[4, 1, i]
       storage[4, 1, i] = colors[3, 1, i]

    colors = np.copy(storage)
    solution.append("e")

def ePrime():

    global colors
    global storage
    
    rotate(pi/2, vector(0, 1, 0), "y", 0, rotatePause)

    for i in range(0, 3):
       storage[3, 1, i] = colors[4, 1, i]
       storage[4, 1, i] = colors[2, 1, i]
       storage[2, 1, i] = colors[5, 1, i]
       storage[5, 1, i] = colors[3, 1, i]

    colors = np.copy(storage)
    solution.append("ePrime")

def s():

    global colors
    global storage
    
    rotate(-pi/2, vector(0, 0, 1), "z", 0, rotatePause)

    for i in range(0, 3):
       storage[1, 1, i] = colors[4, 2-i, 1]
       storage[4, 2-i, 1] = colors[0, 1, 2-i]
       storage[0, 1, 2-i] = colors[5, i, 1]
       storage[5, i, 1] = colors[1, 1, i]

    colors = np.copy(storage)
    solution.append("s")

def sPrime():

    global colors
    global storage
    
    rotate(pi/2, vector(0, 0, 1), "z", 0, rotatePause)

    for i in range(0, 3):
       storage[1, 1, i] = colors[5, i, 1]
       storage[5, i, 1] = colors[0, 1, 2-i]
       storage[0, 1, 2-i] = colors[4, 2-i, 1]
       storage[4, 2-i, 1] = colors[1, 1, i]
       
    colors = np.copy(storage)
    solution.append("sPrime")

def x():

    global colors
    global storage
    
    for n in range(0, 90):
        for i in range(0, 27):
            smallCubeList[i].rotate(angle = -pi/180, axis = vector(1, 0, 0), origin = vector(0, 0, 0))
        time.sleep(rotatePause)

    for i in range(0, 9):
        storage[5, floor(i/3), i%3] = colors[5, 2-(i%3), floor(i/3)]
        storage[4, floor(i/3), i%3] = colors[4, i%3, 2-(floor(i/3))]
            
    for i in range(0, 9):
        storage[0, floor(i/3), i%3] = colors[2, 2-(floor(i/3)), 2-(i%3)]
        storage[2, floor(i/3), i%3] = colors[1, 2-(floor(i/3)), 2-(i%3)]
        storage[1] = colors[3]
        storage[3] = colors[0]

    colors = np.copy(storage)

def y():

    global colors
    global storage
    
    for n in range(0, 90):
        for i in range(0, 27):
            smallCubeList[i].rotate(angle = -pi/180, axis = vector(0, 1, 0), origin = vector(0, 0, 0))
        time.sleep(rotatePause)

    for i in range(0, 9):
        storage[1, floor(i/3), i%3] = colors[1, 2-(i%3), floor(i/3)]
        storage[0, floor(i/3), i%3] = colors[0, i%3, 2-(floor(i/3))]
            
    storage[2] = colors[4]
    storage[4] = colors[3]
    storage[3] = colors[5]
    storage[5] = colors[2]

    colors = np.copy(storage)

def z():

    global colors
    global storage
    
    for n in range(0, 90):
        for i in range(0, 27):
            smallCubeList[i].rotate(angle = -pi/180, axis = vector(0, 0, 1), origin = vector(0, 0, 0))
        time.sleep(rotatePause)

    for i in range(0, 9):
        storage[2, floor(i/3), i%3] = colors[2, i%3, 2-(floor(i/3))]
        storage[3, floor(i/3), i%3] = colors[3, 2-(i%3), floor(i/3)]

    for i in range(0, 9):
        storage[0, floor(i/3), i%3] = colors[5, 2-(i%3), floor(i/3)]
        storage[5, floor(i/3), i%3] = colors[1, 2-(i%3), floor(i/3)]
        storage[1, floor(i/3), i%3] = colors[4, 2-(i%3), floor(i/3)]
        storage[4, floor(i/3), i%3] = colors[0, 2-(i%3), floor(i/3)]

    colors = np.copy(storage)
    solution.append("z")

#exit()
#------------------------------------------------------------------ scramble -----------------------------------------------------------------

def scramble():
    x()
    s()
    l()
    r()
    r()
    ePrime()
    u()
    d()
    rPrime()
    dPrime()
    x()
    s()
    x()
    z()
    x()
    sPrime()
    sPrime()
    x()
    m()
    sPrime()

scrambleList = []    
def pickRandMove(num):
    if (num == 1):
        r()
        scrambleList.append("r")
    if (num == 2):
        rPrime()
        scrambleList.append("rPrime")
    if (num == 3):
        l()
        scrambleList.append("l")
    if (num == 4):
        lPrime()
        scrambleList.append("lPrime")
    if (num == 5):
        u()
        scrambleList.append("u")
    if (num == 6):
        uPrime()
        scrambleList.append("uPrime")
    if (num == 7):
        d()
        scrambleList.append("d")
    if (num == 8):
        dPrime()
        scrambleList.append("dPrime")
    if (num == 9):
        f()
        scrambleList.append("f")
    if (num == 10):
        fPrime()
        scrambleList.append("fPrime")
    if (num == 11):
        b()
        scrambleList.append("b")
    if (num == 12):
        bPrime()
        scrambleList.append("bPrime")
    if (num == 13):
        m()
        scrambleList.append("m")
    if (num == 14):
        mPrime()
        scrambleList.append("mPrime")
    if (num == 15):
        e()
        scrambleList.append("e")
    if (num == 16):
        ePrime()
        scrambleList.append("ePrime")
    if (num == 17):
        s()
        scrambleList.append("s")
    if (num == 18):
        sPrime()
        scrambleList.append("sPrime")
    if (num == 19):
        x()
        scrambleList.append("x")
    if (num == 20):
        y()
        scrambleList.append("y")
    if (num == 21):
        z()
        scrambleList.append("z")
    
randScramble = input("Would you like this scramble to be random? (yes or no) \n⟶ ").lower()

if (randScramble == "yes"):
    for i in range(20):
        pickRandMove(random.randint(1, 21))
    time.sleep(stagePause)
else:
    scramble()
    if (input("Is this the correct scramble? (yes or no) \n⟶ ").lower() == "no"):
        print("You can fix it now.")
        exit()

time.sleep(0.5)

#exit()
#------------------------------------------------------------- cube orientation -------------------------------------------------------------

def cubeOrientation(front, top):
    for i in range(0, 4):
        if (colors[3, 1, 1] == front):
            break
        y()
        
    if (colors[3, 1, 1] != front):
        for i in range(0, 4):
            if (colors[3, 1, 1] == front):
                break
            x()
        
    while (colors[1, 1, 1] != top):
        z()

cubeOrientation("g", "y")

#exit()
#---------------------------------------------------------------- white cross ----------------------------------------------------------------

def orientation(zValue, yValue, xValue):
    if (zValue == 2 or (zValue == 1 and yValue == 0)):
            y()
            y()
    if (zValue == 4 or (zValue == 1 and yValue == 1 and xValue == 0)):
            y()
            y()
            y()
    if (zValue == 5 or (zValue == 1 and yValue == 1 and xValue == 2)):
            y()

def reorientation(zValue, yValue, xValue):
    if (zValue == 2 or (zValue == 1 and yValue == 0)):
            y()
            y()
    if (zValue == 4 or (zValue == 1 and yValue == 1 and xValue == 0)):
            y()
    if (zValue == 5 or (zValue == 1 and yValue == 1 and xValue == 2)):
            y()
            y()
            y()

def yellowFaceEdge(EdgeZ, EdgeY, EdgeX):
    if (colors[EdgeZ, EdgeY, EdgeX] == "w"):
        orientation(EdgeZ, EdgeY, EdgeX)
        while (colors[0, 0, 1] == "w"):
            d()
        f()
        f()
        reorientation(EdgeZ, EdgeY, EdgeX)

def adjYellowFaceEdge(EdgeZ, EdgeY, EdgeX):
    if (colors[EdgeZ, EdgeY, EdgeX] == "w"):
        orientation(EdgeZ, EdgeY, EdgeX)
        while (colors[0, 0, 1] == "w"):
            d()
        f()
        d()
        rPrime()
        dPrime()
        reorientation(EdgeZ, EdgeY, EdgeX)

def middleRightEdge(EdgeZ, EdgeY, EdgeX):
    if (colors[EdgeZ, EdgeY, EdgeX] == "w"):
        orientation(EdgeZ, EdgeY, EdgeX)
        while (colors[0, 1, 2] == "w"):
            d()
        rPrime()
        reorientation(EdgeZ, EdgeY, EdgeX)
            
def middleLeftEdge(EdgeZ, EdgeY, EdgeX):
    if (colors[EdgeZ, EdgeY, EdgeX] == "w"):
        orientation(EdgeZ, EdgeY, EdgeX)
        while (colors[0, 1, 0] == "w"):
            d()
        l()
        reorientation(EdgeZ, EdgeY, EdgeX)

def bottomEdge(EdgeZ, EdgeY, EdgeX):
    if (colors[EdgeZ, EdgeY, EdgeX] == "w"):
        orientation(EdgeZ, EdgeY, EdgeX)
        fPrime()
        d()
        rPrime()
        dPrime()
        reorientation(EdgeZ, EdgeY, EdgeX)

#exit()
while (colors[0, 2, 1] != "w" or colors[0, 0, 1] != "w" or colors[0, 1, 0] != "w" or colors[0, 1, 2] != "w"):
    
    #yellowFaceEdge
    yellowFaceEdge(1, 0, 1)
    yellowFaceEdge(1, 2, 1)
    yellowFaceEdge(1, 1, 0)
    yellowFaceEdge(1, 1, 2)

    #adjYellowFaceEdge
    adjYellowFaceEdge(2, 0, 1)
    adjYellowFaceEdge(3, 0, 1)
    adjYellowFaceEdge(4, 0, 1)
    adjYellowFaceEdge(5, 0, 1)

    #middleRightEdge
    middleRightEdge(2, 1, 2)
    middleRightEdge(3, 1, 2)
    middleRightEdge(4, 1, 2)
    middleRightEdge(5, 1, 2)
        
    #middleLeftEdge
    middleLeftEdge(4, 1, 0)
    middleLeftEdge(5, 1, 0)
    middleLeftEdge(3, 1, 0)
    middleLeftEdge(2, 1, 0)
        
    #bottomEdge
    bottomEdge(2, 2, 1)
    bottomEdge(3, 2, 1)
    bottomEdge(4, 2, 1)
    bottomEdge(5, 2, 1)
        
time.sleep(stagePause)

#exit()
#---------------------------------------------------------- white cross orientation ----------------------------------------------------------

cubeOrientation("g", "y")
    
def oppSwitchAlg():
    r()
    r()
    l()
    l()
    d()
    d()
    r()
    r()
    l()
    l()
    while (corColors.count(1) != 4):
        d()
        countCor()

def adjSwitchAlg():
    r()
    d()
    rPrime()
    dPrime()
    r()

def countCor():
    
    global corColors
    corColors = []
    
    for i in range(2, 6):
        if (colors[i, 2, 1] == colors[i, 1, 1]):
            corColors.append(1)
        else:
            corColors.append(0)

corColors = []
  
countCor()       
while (corColors.count(1) < 2):
    d()
    countCor()
    
if (corColors.count(1) == 2):
    
    if (corColors == [1, 1, 0, 0] or corColors == [0, 0, 1, 1]):
        oppSwitchAlg()
        
    if (corColors == [1, 0, 1, 0]):
        adjSwitchAlg()
        
    if (corColors == [0, 1, 1, 0]):
        y()
        adjSwitchAlg()
        
    if (corColors == [0, 1, 0, 1]):
        y()
        y()
        adjSwitchAlg()
        
    if (corColors == [1, 0, 0, 1]):
        y()
        y()
        y()
        adjSwitchAlg()
        
time.sleep(stagePause)

#exit()
#--------------------------------------------------------------- white corners ---------------------------------------------------------------

cubeOrientation("g", "y")

def insTopCorners():
    
    while (colors[0, 0, 0] != "w" or colors[0, 0, 2] != "w" or colors[0, 2, 0] != "w" or colors[0, 2, 2] != "w"):

        if (colors[3, 0, 2] == "w"):
            counter = 0
            while (colors[5, 0, 0] != colors[5, 1, 1]):
                e()
                dPrime()
                counter += 1
            fPrime()
            uPrime()
            f()
            for n in range(0, counter):
                ePrime()
                d()
            continue

        if (colors[5, 0, 0] == "w"):
            counter = 0
            while (colors[3, 0, 2] != colors[3, 1, 1]):
                e()
                dPrime()
                counter += 1
                #print(1) #did 1 while loop
            r()
            u()
            rPrime()
            for i in range(0, counter):
                ePrime()
                d()
            continue

        if (colors[1, 2, 2] == "w"):
            counter = 0
            while (colors[3, 0, 2] != colors[5, 1, 1]):
                e()
                dPrime()
                counter += 1
                #print(1)
            r()
            u()
            u()
            rPrime()
            uPrime()
            r()
            u()
            rPrime()
            for i in range(0, counter):
                ePrime()
                d()
            continue

        y()

#exit()
for i in range(0, 4):
        
        if ((colors[3, 2, 2] == "w" or colors[5, 2, 0] == "w" or colors[0, 0, 2] == "w") and (colors[0, 0, 2] != "w" or colors[5, 2, 0] != colors[5, 1, 1] or colors[3, 2, 2] != colors[3, 1, 1])):
            while (colors[3, 0, 2] == "w" or colors[5, 0, 0] == "w" or colors[1, 2, 2] == "w"):
                u()
                #print(1)
            r()
            u()
            rPrime()

        y()

#exit()
insTopCorners()
        
time.sleep(stagePause)

#exit()
#--------------------------------------------------------------- middle edges ---------------------------------------------------------------

cubeOrientation("g", "y")

def rightEdgeInsAlg():
    u()
    r()
    uPrime()
    rPrime()
    uPrime()
    fPrime()
    u()
    f()

def leftEdgeInsAlg():
    uPrime()
    lPrime()
    u()
    l()
    u()
    f()
    uPrime()
    fPrime()
    
for i in range(0, 4):
    if (colors[3, 1, 0] != "y" and colors[4, 1, 2] != "y" and (colors[3, 1, 0] != colors[3, 1, 1] or colors[4, 1, 2] != colors[4, 1, 1])):
        while (colors[3, 0, 1] != "y" and colors[1, 2, 1] != "y"):
            u()
        leftEdgeInsAlg()
    y()

#exit()
while ((colors[3, 1, 0] != colors[3, 1, 1] or colors[4, 1, 2] != colors[4, 1, 1]) or (colors[3, 1, 2] != colors[3, 1, 1] or colors[5, 1, 0] != colors[5, 1, 1]) or (colors[4, 1, 0] != colors[4, 1, 1] or colors[2, 1, 2] != colors[2, 1, 1]) or (colors[4, 1, 2] != colors[4, 1, 1] or colors[2, 1, 0] != colors[2, 1, 1])):
    for i in range(0, 4):
        for n in range(0, 4):
            if (colors[3, 0, 1] == colors[3, 1, 1] and colors[1, 2, 1] == colors[5, 1, 1]):
                rightEdgeInsAlg()
            if (colors[3, 0, 1] == colors[3, 1, 1] and colors[1, 2, 1] == colors[4, 1, 1]):
                leftEdgeInsAlg()
            if (colors[3, 0, 1] == colors[3, 1, 1] and colors[1, 2, 1] == colors[5, 1, 1]):
                rightEdgeInsAlg()
            u()
        y()
        
time.sleep(stagePause)

#exit()
#--------------------------------------------------------------- yellow cross ---------------------------------------------------------------

cubeOrientation("g", "y")

def solveL():
    f()
    u()
    r()
    uPrime()
    rPrime()
    fPrime()

def solveI():
    f()
    r()
    u()
    rPrime()
    uPrime()
    fPrime()
    
if (colors[1, 0, 1] != "y" and colors[1, 1, 0] != "y" and colors[1, 1, 2] != "y" and colors[1, 2, 1] != "y"):
    solveL()

while (colors[1, 0, 1] != "y"):
    u()

if (colors[1, 1, 0] == "y" and colors[1, 2, 1] != "y"):
    solveL()
elif (colors[1, 1, 2] == "y" and colors[1, 2, 1] != "y"):
    uPrime()
    solveL()
elif (colors[1, 2, 1] == "y" and colors[1, 1, 2] != "y"):
    u()
    solveI()
        
time.sleep(stagePause)

#exit()
#--------------------------------------------------------------- yellow corners ---------------------------------------------------------------

cubeOrientation("g", "y")

#algorithms
def tShirt():
    uPrime()
    r()
    u()
    u()
    r()
    r()
    uPrime()
    r()
    r()
    uPrime()
    r()
    r()
    u()
    u()
    r()

def doubleSune():
    r()
    u()
    rPrime()
    u()
    r()
    uPrime()
    rPrime()
    u()
    r()
    u()
    u()
    rPrime()

def antisune():
    lPrime()
    uPrime()
    l()
    uPrime()
    lPrime()
    u()
    u()
    l()

def backwardAntisune():
    b()
    u()
    bPrime()
    u()
    b()
    u()
    u()
    bPrime()

def hammerhead():
    m()
    r()
    u()
    rPrime()
    uPrime()
    mPrime()
    rPrime()
    f()
    r()
    fPrime()

def headlights():
    uPrime()
    r()
    r()
    d()
    rPrime()
    u()
    u()
    r()
    dPrime()
    rPrime()
    u()
    u()
    rPrime()

def diagonals():
    f()
    rPrime()
    fPrime()
    m()
    r()
    u()
    r()
    uPrime()
    mPrime()
    rPrime()

if (colors[1, 0, 0] == "y" or colors[1, 0, 2] == "y" or colors[1, 2, 0] == "y" or colors[1, 2, 2] == "y"):
    while (colors[1, 2, 2] != "y"):
        u()

#exit()
#no yellow corners
if (colors[1, 0, 0] != "y" and colors[1, 0, 2] != "y" and colors[1, 2, 0] != "y" and colors[1, 2, 2] != "y"):
    while (colors[3, 0, 0] == "y" or colors[3, 0, 2] == "y"):
        u()
    if (colors[2, 0, 0] == "y"):
        tShirt()
    else:
        doubleSune()
#one yellow corner
elif (colors[1, 0, 0] != "y" and colors[1, 0, 2] != "y" and colors[1, 2, 0] != "y"):
    if (colors[3, 0, 0] == "y"):
        antisune()
    else:
        backwardAntisune()
#two adjacent yellow corners
elif ((colors[1, 2, 0] == "y" or colors[1, 0, 2] == "y") and colors[1, 0, 0] != "y"):
    if (colors[1, 2, 0] == "y"):
        uPrime()
    if (colors[3, 0, 0] == "y"):
        hammerhead()
    if (colors[4, 0, 0] == "y"):
        headlights()
#two opposite yellow corners
elif (colors[1, 0, 0] == "y" and colors[1, 2, 0] != "y"):
    if (colors[3, 0, 0] != "y"):
        u()
        u()
    diagonals()
        
time.sleep(stagePause)

#exit()
#--------------------------------------------------------------- last layer corners ---------------------------------------------------------------

cubeOrientation("g", "y")

def findCorners():
    corners = []
    for i in range(4):
        if (colors[3, 0, 0] == colors[3, 1, 1] and colors[4, 0, 2] == colors[4, 1, 1]):
            corners.append(1)
        else:
            corners.append(0)
        y()
    return corners

def adjOrOpp(array):
    for i in range(4):
        if (array[0] == 0):
            del array[0]
            array.insert(3, 0)
    if (array[2] == 1 and array[3] == 0):
        return "opp"
    elif ((array[1] == 1 or array[3] == 1) and array[2] == 0):
        return "adj"
    else:
        return "nope"

def fixCorners():
    rPrime()
    f()
    rPrime()
    b()
    b()
    r()
    fPrime()
    rPrime()
    b()
    b()
    r()
    r()

while (sum(findCorners()) != 4):
    
    while (sum(findCorners()) < 2):
        u()

    if (adjOrOpp(findCorners()) == "adj"):
        while (colors[2, 0, 0] != colors[2, 0, 2]):
            u()
        while (colors[2, 0, 0] != colors[2, 1, 1]):
            e()
            dPrime()
        fixCorners()
        uPrime()
        
    elif (adjOrOpp(findCorners()) == "opp"):
        fixCorners()
           
time.sleep(stagePause)
 
#exit()
#--------------------------------------------------------------- last layer edges ---------------------------------------------------------------

cubeOrientation("g", "y")

#algorithms
def hPerm():
    m()
    m()
    u()
    m()
    m()
    u()
    u()
    m()
    m()
    u()
    m()
    m()

def zPerm():
    m()
    m()
    u()
    m()
    m()
    u()
    mPrime()
    u()
    u()
    m()
    m()
    u()
    u()
    mPrime()
    u()
    u()

def ubPerm():
    m()
    m()
    u()
    mPrime()
    u()
    u()
    m()
    u()
    m()
    m()

def uaPerm():
    m()
    m()
    uPrime()
    mPrime()
    u()
    u()
    m()
    uPrime()
    m()
    m()

if (colors[2, 0, 1] != colors[2, 1, 1] and colors[3, 0, 1] != colors[3, 1, 1] and colors[4, 0, 1] != colors[4, 1, 1] and colors[5, 0, 1] != colors[5, 1, 1]):
    if (colors[3, 0, 1] == colors[2, 1, 1]):
        hPerm()
    else:
        while(colors[3, 0, 1] != colors[4, 1, 1]):
            y()
        zPerm()
elif ((colors[2, 0, 1] == colors[2, 1, 1] or colors[3, 0, 1] == colors[3, 1, 1] or colors[4, 0, 1] == colors[4, 1, 1] or colors[5, 0, 1] == colors[5, 1, 1]) and not (colors[2, 0, 1] == colors[2, 1, 1] and colors[3, 0, 1] == colors[3, 1, 1] and colors[4, 0, 1] == colors[4, 1, 1] and colors[5, 0, 1] == colors[5, 1, 1])):
    while (colors[2, 0, 1] != colors[2, 1, 1]):
        y()
    if (colors[3, 1, 1] == colors[4, 0, 1]):
        uaPerm()
    else:
        ubPerm()

cubeOrientation("g", "y")

#exit()
#--------------------------------------------------------------- editing solution ---------------------------------------------------------------

solution2 = solution.copy()

c = 0

while (c <= len(solution) - 4):
    
    if (solution[c] == solution[c + 1] == solution[c + 2] == solution[c + 3]):
        np.delete(solution2, c)
        np.delete(solution2, c + 1)
        np.delete(solution2, c + 2)
        np.delete(solution2, c + 3)
        solution = solution2.copy()
        
    c += 1

'''c = 0

while (c <= len(solution) - 3):
    
    if (solution[c] == solution[c + 1] == solution[c + 2] == solution[c + 3]):
        if ("Prime" in solution[c]):
            solution2[c] = solution2[c][0]
        else:
            solution2[c] = solution2[c] + "'"
            
        np.delete(solution2, c + 1)
        np.delete(solution2, c + 1)
        solution = np.copy(solution2)

    c += 1'''

#printing scramble + solution
print("Cube is solved!")
printSolScr = input("Would you like to see the scramble and solution? (yes or no) \n⟶ ").lower()
if (printSolScr == "yes"):
    print("scramble: ", scrambleList)
    print()
    print("solution: ", solution)

import leg as leg
import math as math
from time import sleep

def balloon(keyframe, leg, statusValues):
    stepWidth = 130

    startPos = [statusValues[2], 0, statusValues[3]]
    startPosX = startPos[0]
    startPosY = startPos[1]
    startPosZ = startPos[2]
    
    # keyframe 0 is for setup
    if keyframe == 0:
        # set legs to default position
        leg.changePos(startPosX, startPosY, startPosZ, add=False, apply=False, invertX=False)

        if leg.id == 3 or leg.id == 6:
            leg.changePos(startPosX + 0, startPosY + (stepWidth / 2), startPosZ, add=False)
        elif leg.id == 2 or leg.id == 5:
            leg.changePos(startPosX + 0, startPosY - stepWidth, startPosZ + 60, add=False)
        elif leg.id == 1 or leg.id == 4:
            leg.changePos(startPosX + 0, startPosY - (stepWidth / 2), startPosZ + 0, add=False)

    if keyframe == 1:
        if leg.id == 1 or leg.id == 4:
            leg.changePos(0, 0, 200, offset=False)
            
    elif keyframe == 2:
        if leg.id == 1 or leg.id == 4:
            leg.changePos(-50, -stepWidth / 1.3, 0, offset=False)
            
    elif keyframe == 3:
        if leg.id == 1 or leg.id == 4:
            leg.changePos(50, stepWidth / 1.3, -200, offset=False)

def rotate(keyframe, leg, statusValues):
    stepWidth = 138
    stepHeight = 30 *-1
    
    if statusValues[1] == "right":
        stepWidth *= -1

    startPos = [statusValues[2], 0, statusValues[3]]
    startPosX = startPos[0]
    startPosY = startPos[1]
    startPosZ = startPos[2]

    offset = False

    if keyframe == 0:
        if leg.id == 2:
            leg.changePos(startPosX, startPosY - (stepWidth / 2), startPosZ, add=False, apply=False, invertX=False, offset=False)
            
        elif leg.id == 4 or leg.id == 6:
            leg.changePos(startPosX, startPosY + (stepWidth / 2), startPosZ, add=False, apply=False, invertX=False, offset=False)
            
        elif leg.id == 1 or leg.id == 3:
            leg.changePos(startPosX, startPosY - (stepWidth / 2), startPosZ, add=False, apply=False, invertX=False, offset=False)
            
        elif leg.id == 5:
            leg.changePos(startPosX, startPosY + (stepWidth / 2), startPosZ, add=False, apply=False, invertX=False, offset=False)

    elif keyframe == 1:
        if leg.id == 2:
            leg.changePos(startPosX, startPosY, startPosZ, add=False, offset=False)

        elif leg.id == 4 or leg.id == 6:
            leg.changePos(startPosX, startPosY, startPosZ, add=False, offset=False)
            
        elif leg.id == 1 or leg.id == 3:
            leg.changePos(startPosX, startPosY - (stepWidth / 2), startPosZ + stepHeight, add=False, offset=False)
            
        elif leg.id == 5:
            leg.changePos(startPosX, startPosY + (stepWidth / 2), startPosZ + stepHeight, add=False, offset=False)
            
    elif keyframe == 2:
        if leg.id == 2:
            leg.changePos(startPosX, startPosY + (stepWidth / 2), startPosZ, add=False, offset=False)
            
        elif leg.id == 4 or leg.id == 6:
            leg.changePos(startPosX, startPosY - (stepWidth / 2), startPosZ, add=False, offset=False)
            
        elif leg.id == 1 or leg.id == 3:
            leg.changePos(startPosX, startPosY - (stepWidth / 2), startPosZ, add=False, offset=False)
            
        elif leg.id == 5:
            leg.changePos(startPosX, startPosY + (stepWidth / 2), startPosZ, add=False, offset=False)

    elif keyframe == 3:
        if leg.id == 2:
            leg.changePos(startPosX, startPosY - (stepWidth / 2), startPosZ + stepHeight, add=False, offset=False)
            
        elif leg.id == 4 or leg.id == 6:
            leg.changePos(startPosX, startPosY + (stepWidth / 2), startPosZ + stepHeight, add=False, offset=False)
            
        elif leg.id == 1 or leg.id == 3:
            leg.changePos(startPosX, startPosY, startPosZ, add=False, offset=False)
            
        elif leg.id == 5:
            leg.changePos(startPosX, startPosY, startPosZ, add=False, offset=False)

    elif keyframe == 4:
        if leg.id == 2:
            leg.changePos(startPosX, startPosY - (stepWidth / 2), startPosZ, add=False, offset=False)
            
        elif leg.id == 4 or leg.id == 6:
            leg.changePos(startPosX, startPosY + (stepWidth / 2), startPosZ, add=False, offset=False)
            
        elif leg.id == 1 or leg.id == 3:
            leg.changePos(startPosX, startPosY - (stepWidth / 2), startPosZ, add=False, offset=False)
            
        elif leg.id == 5:
            leg.changePos(startPosX, startPosY + (stepWidth / 2), startPosZ, add=False, offset=False)
            
def idle(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.changePos(statusValues[2], 0, statusValues[3], add=False, invertX=False)

#poortje
#leg.changePos(130,0,110, add=False)

#grindbak
#leg.changePos(130,0,150, add=False)
    

def walk(keyframe, leg, statusValues):
    stepWidth = 70
    isWalking = True

    if statusValues[1] == "left":
        isWalking = False
        if leg.id == 1 or leg.id == 2 or leg.id == 3:
            stepWidth *= -2
    elif statusValues[1] == "right":
        isWalking = False
        if leg.id == 4 or leg.id == 5 or leg.id == 6:
            stepWidth *= -2

    stepHeight = 60 *-1
    radfactor = math.pi / 180
    stepWidthY = stepWidth * math.cos(statusValues[0] * radfactor)
    stepWidthX = stepWidth * math.sin(statusValues[0] * radfactor)

    
    startPos = [statusValues[2], 0, statusValues[3]]
    startPosX = startPos[0]
    startPosY = startPos[1]
    startPosZ = startPos[2]
    
    # keyframe 0 is for setup
    if keyframe == 0:
        # set legs to default position
        leg.changePos(startPosX, startPosY, startPosZ, add=False, apply=False, invertX=False, offset=isWalking)

        if leg.isEven():
            leg.changePos(startPosX - (stepWidthX / 2), startPosY - (stepWidthY / 2), startPosZ - 0, add=False, offset=isWalking)
            
        else:
            leg.changePos(startPosX + (stepWidthX / 2), startPosY + (stepWidthY / 2), startPosZ + 0, add=False, offset=isWalking)
        
    elif keyframe == 1:
        if leg.isEven():
            leg.changePos(startPosX, startPosY, startPosZ, add=False, offset=isWalking)
        else:
            leg.changePos(startPosX, startPosY, startPosZ + stepHeight, add=False, offset=isWalking)
        
    elif keyframe == 2:
        if leg.isEven():
            leg.changePos(startPosX + (stepWidthX / 2), startPosY + (stepWidthY / 2), startPosZ, add=False, offset=isWalking)
        else:
            leg.changePos(startPosX - (stepWidthX / 2), startPosY - (stepWidthY / 2), startPosZ, add=False, offset=isWalking)
        
    elif keyframe == 3:
        if leg.isEven():
            leg.changePos(startPosX, startPosY, startPosZ + stepHeight, add=False, offset=isWalking)
        else:
            leg.changePos(startPosX, startPosY, startPosZ, add=False, offset=isWalking)
        
    elif keyframe == 4:
        if leg.isEven():
            leg.changePos(startPosX - (stepWidthX / 2), startPosY - (stepWidthY / 2), startPosZ, add=False, offset=isWalking)
        else:
            leg.changePos(startPosX + (stepWidthX / 2), startPosY + (stepWidthY / 2), startPosZ, add=False, offset=isWalking)

def fly(keyframe,leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)

    elif keyframe == 1:
        leg.setAngles(512,819,538)
    elif keyframe == 2:
        leg.setAngles(512,819,380)
        
def dab(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)
        if leg.id == 3 or leg.id == 6:
            leg.setAngles(406,678,345)
        elif leg.id == 2 or leg.id == 5:
            leg.setAngles(590,538,459)

    elif keyframe == 1:
        if leg.id == 1:
            leg.setAngles(915,520,679)
        elif leg.id == 4:
            leg.setAngles(283,555,634)
    elif keyframe == 2:
        if leg.id == 1:
            leg.setAngles(590,661,748)
        elif leg.id == 4:
            leg.setAngles(143,512,749)
            
def leftToRight(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)

    elif keyframe == 1:
        if leg.id == 1 or leg.id == 2 or leg.id == 3:
            leg.setAngles(512,609,547)
        elif leg.id == 4 or leg.id == 5 or leg.id == 6:
            leg.setAngles(512,433,556)
    elif keyframe == 2:
        if leg.id == 1 or leg.id == 2 or leg.id == 3:
            leg.setAngles(512,433,556)
        elif leg.id == 4 or leg.id == 5 or leg.id == 6:
            leg.setAngles(512,609,547)
            
def rightToLeft(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)

    elif keyframe == 1:
        if leg.id == 1 or leg.id == 2 or leg.id == 3:
            leg.setAngles(512,433,556)
        elif leg.id == 4 or leg.id == 5 or leg.id == 6:
            leg.setAngles(512,609,547)
    elif keyframe == 2:
        if leg.id == 1 or leg.id == 2 or leg.id == 3:
            leg.setAngles(512,609,547)
        elif leg.id == 4 or leg.id == 5 or leg.id == 6:
            leg.setAngles(512,433,556)

def frontToBack(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)

    elif keyframe == 1:
        if leg.id == 1 or leg.id == 4:
            leg.setAngles(512,775,257)
        elif leg.id == 2 or leg.id == 5:
            leg.setAngles(512,635,389)
        elif leg.id == 3 or leg.id == 6:
            leg.setAngles(512,459,565)
    elif keyframe == 2:
        if leg.id == 1 or leg.id == 4:
            leg.setAngles(512,459,565)
        elif leg.id == 2 or leg.id == 5:
            leg.setAngles(512,635,389)
        elif leg.id == 3 or leg.id == 6:
            leg.setAngles(512,775,257)

def backToFront(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)

    elif keyframe == 1:
        if leg.id == 1 or leg.id == 4:
            leg.setAngles(512,459,565)
        elif leg.id == 2 or leg.id == 5:
            leg.setAngles(512,635,389)
        elif leg.id == 3 or leg.id == 6:
            leg.setAngles(512,775,257)
    elif keyframe == 2:
        if leg.id == 1 or leg.id == 4:
            leg.setAngles(512,775,257)
        elif leg.id == 2 or leg.id == 5:
            leg.setAngles(512,635,389)
        elif leg.id == 3 or leg.id == 6:
            leg.setAngles(512,459,565)

def downToUp(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)

    elif keyframe == 1:
        leg.setAngles(512,837,196)
    elif keyframe == 2:
        leg.setAngles(512,301,731)

def upToDown(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)
        
    elif keyframe == 1:
        leg.setAngles(512,301,731)
    elif keyframe == 2:
        leg.setAngles(512,837,196)

def hipsToLeft(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)
        
    elif keyframe == 1:
            leg.setAngles(397,512,512)
    elif keyframe == 2:
            leg.setAngles(608,837,196)



def hipsToRight(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)
        
    elif keyframe == 1:
            leg.setAngles(608,837,196)     
    elif keyframe == 2:
            leg.setAngles(397,512,512)
            
def wave(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)

    elif keyframe == 1:
        if leg.id == 1 or leg.id == 4:
            leg.setAngles(512,459,565)
        elif leg.id == 2 or leg.id == 5:
            leg.setAngles(512,635,389)
        elif leg.id == 3 or leg.id == 6:
            leg.setAngles(512,775,257)
    elif keyframe == 2:
        leg.setAngles(512,459,565)
    elif keyframe == 3:
        if leg.id == 1 or leg.id == 4:
            leg.setAngles(512,775,257)
        elif leg.id == 2 or leg.id == 5:
            leg.setAngles(512,635,389)
        elif leg.id == 3 or leg.id == 6:
            leg.setAngles(512,459,565)
    elif keyframe == 4:
        leg.setAngles(512,775,257)
        
def waveInverse(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)

    elif keyframe == 1:
        if leg.id == 1 or leg.id == 4:
            leg.setAngles(512,775,257)
        elif leg.id == 2 or leg.id == 5:
            leg.setAngles(512,635,389)
        elif leg.id == 3 or leg.id == 6:
            leg.setAngles(512,459,565)
    elif keyframe == 2:
        leg.setAngles(512,775,257)
    elif keyframe == 3:
        if leg.id == 1 or leg.id == 4:
            leg.setAngles(512,459,565)
        elif leg.id == 2 or leg.id == 5:
            leg.setAngles(512,635,389)
        elif leg.id == 3 or leg.id == 6:
            leg.setAngles(512,775,257)
    elif keyframe == 4:
        leg.setAngles(512,459,565)

def twerk(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)
        if leg.id == 1 or leg.id == 4:
            leg.setAngles(512,775,257)
        elif leg.id == 2 or leg.id == 5:
            leg.setAngles(512,635,389)
        elif leg.id == 3 or leg.id == 6:
            leg.setAngles(512,459,565)
            
    elif keyframe == 1:
        if leg.id == 3 or leg.id == 6:
            leg.setAngles(512,635,389)         
    elif keyframe == 2:
        if leg.id == 3 or leg.id == 6:
            leg.setAngles(512,459,565)

def greet(keyframe, leg, statusValues):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)
        if leg.id == 2:
            leg.setAngles(696,512,512)
        elif leg.id == 1:
            leg.setAngles(722,714,767)

    elif keyframe == 1:
        if leg.id == 1:
            leg.setAngles(916,714,688)

    elif keyframe == 2:
        if leg.id == 1:
            leg.setAngles(722,714,767)

import leg2 as leg
import math as math
from time import sleep

def balloon(keyframe, leg, angle):
    stepWidth = 130
    
    # keyframe 0 is for setup
    if keyframe == 0:
        if leg.id == 3 or leg.id == 6:
            leg.changePos(0, stepWidth /2, 60, invertX=False)
        elif leg.id == 2 or leg.id == 5:
            leg.changePos(0, -stepWidth, 0, invertX=False)
        elif leg.id == 1 or leg.id == 4:
            leg.changePos(0, -stepWidth / 2, 0, invertX=False)

    if keyframe == 1:
        if leg.id == 1 or leg.id == 4:
            leg.changePos(0, 0, 200, offset=False)
            
    elif keyframe == 2:
        if leg.id == 1 or leg.id == 4:
            leg.changePos(-50, -stepWidth / 1.3, 0, offset=False)
            
    elif keyframe == 3:
        if leg.id == 1 or leg.id == 4:
            leg.changePos(50, stepWidth / 1.3, -200, offset=False)

def rotate(keyframe, leg, direction = -1):
    stepWidth = 54
    stepHeight = 30

    offset = False

    if keyframe == 0:
        if leg.id == 2:
            leg.changePos(0, -stepWidth / 2, 0, offset=False)
            
        elif leg.id == 4 or leg.id == 6:
            leg.changePos(0, stepWidth / 2, 0, offset=False)
            
        elif leg.id == 1 or leg.id == 3:
            leg.changePos(0, -stepWidth / 2, 0, offset=False)
            
        elif leg.id == 5:
            leg.changePos(0, stepWidth / 2, 0, offset=False)

    elif keyframe == 1:
        if leg.id == 2:
            leg.changePos(0, stepWidth / 2, 0, offset=False)
            
        elif leg.id == 4 or leg.id == 6:
            leg.changePos(0, -stepWidth / 2, 0, offset=False)
            
        elif leg.id == 1 or leg.id == 3:
            leg.changePos(0, -stepWidth, stepHeight, offset=False)
            
        elif leg.id == 5:
            leg.changePos(0, stepWidth, stepHeight, offset=False)
            
    elif keyframe == 2:
        if leg.id == 2:
            leg.changePos(0, stepWidth / 2, 0, offset=False)
            
        elif leg.id == 4 or leg.id == 6:
            leg.changePos(0, -stepWidth / 2, 0, offset=False)
            
        elif leg.id == 1 or leg.id == 3:
            leg.changePos(0, 0, -stepHeight, offset=False)
            
        elif leg.id == 5:
            leg.changePos(0, 0, -stepHeight, offset=False)

    elif keyframe == 3:
        if leg.id == 2:
            leg.changePos(0, -stepWidth, stepHeight)
            
        elif leg.id == 4 or leg.id == 6:
            leg.changePos(0, stepWidth, stepHeight, offset=False)
            
        elif leg.id == 1 or leg.id == 3:
            leg.changePos(0, stepWidth / 2, 0, offset=False)
            
        elif leg.id == 5:
            leg.changePos(0, -stepWidth / 2, 0, offset=False)

    elif keyframe == 4:
        if leg.id == 2:
            leg.changePos(0, 0, -stepHeight, offset=False)
            
        elif leg.id == 4 or leg.id == 6:
            leg.changePos(0, 0, -stepHeight, offset=False)
            
        elif leg.id == 1 or leg.id == 3:
            leg.changePos(0, stepWidth / 2, 0, offset=False)
            
        elif leg.id == 5:
            leg.changePos(0, -stepWidth / 2, 0, offset=False)
            
def idle(keyframe,leg):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.changePos(130,0,110, add=False, invertX=False)

#poortje
#leg.changePos(130,0,110, add=False)

#grindbak
#leg.changePos(130,0,150, add=False)
    

def walk(keyframe, leg, angle):
    stepWidth = 70  
    stepHeight = 60 *-1
    radfactor = math.pi / 180
    stepWidthY = stepWidth * math.cos(angle * radfactor)
    stepWidthX = stepWidth * math.sin(angle * radfactor)

    startPos = [130,0,110]
    startPosX = startPos[0]
    startPosY = startPos[1]
    startPosZ = startPos[2]
    
    # keyframe 0 is for setup
    if keyframe == 0:
        # set legs to default position
        leg.changePos(130,0,110, add=False, apply=False, invertX=False)

        if leg.isEven():
            leg.changePos(startPosX - (stepWidthX / 2), startPosY - (stepWidthY / 2), startPosZ - 0, add=False)
            
        else:
            leg.changePos(startPosX + (stepWidthX / 2), startPosY + (stepWidthY / 2), startPosZ + 0, add=False)
        
    elif keyframe == 1:
        if leg.isEven():
            #leg.changePos(stepWidthX / 2, stepWidthY / 2, 0)
            leg.changePos(startPosX, startPosY, startPosZ, add=False)
        else:
            #leg.changePos(-stepWidthX / 2, -stepWidthY / 2, stepHeight)
            leg.changePos(startPosX, startPosY, startPosZ + stepHeight, add=False)
        
    elif keyframe == 2:
        if leg.isEven():
            #leg.changePos(stepWidthX / 2, stepWidthY / 2, 0)
            leg.changePos(startPosX + (stepWidthX / 2), startPosY + (stepWidthY / 2), startPosZ, add=False)
        else:
            #leg.changePos(-stepWidthX / 2, -stepWidthY / 2, -stepHeight)
            leg.changePos(startPosX - (stepWidthX / 2), startPosY - (stepWidthY / 2), startPosZ, add=False)
        
    elif keyframe == 3:
        if leg.isEven():
            #leg.changePos(-stepWidthX / 2, -stepWidthY / 2, stepHeight)
            leg.changePos(startPosX, startPosY, startPosZ + stepHeight, add=False)
        else:
            #leg.changePos(stepWidthX / 2, stepWidthY / 2, 0)
            leg.changePos(startPosX, startPosY, startPosZ, add=False)
        
    elif keyframe == 4:
        if leg.isEven():
            #leg.changePos(-stepWidthX / 2, -stepWidthY / 2, -stepHeight)
            leg.changePos(startPosX - (stepWidthX / 2), startPosY - (stepWidthY / 2), startPosZ, add=False)
        else:
            #leg.changePos(stepWidthX / 2, stepWidthY / 2, 0)
            leg.changePos(startPosX + (stepWidthX / 2), startPosY + (stepWidthY / 2), startPosZ, add=False)

def fly(keyframe,leg):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)

    elif keyframe == 1:
        leg.setAngles(512,819,538)
    elif keyframe == 2:
        leg.setAngles(512,819,380)
        
def dab(keyframe,leg,angle):
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
            
def leftToRight(keyframe,leg):
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
            
def rightToLeft(keyframe,leg):
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

def frontToBack(keyframe,leg):
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

def backToFront(keyframe,leg):
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

def downToUp(keyframe,leg):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)

    elif keyframe == 1:
        leg.setAngles(512,837,196)
    elif keyframe == 2:
        leg.setAngles(512,301,731)

def upToDown(keyframe,leg):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)
        
    elif keyframe == 1:
        leg.setAngles(512,301,731)
    elif keyframe == 2:
        leg.setAngles(512,837,196)

def hipsToLeft(keyframe,leg):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)
        
    elif keyframe == 1:
            leg.setAngles(397,512,512)
    elif keyframe == 2:
            leg.setAngles(608,837,196)



def hipsToRight(keyframe,leg):
    # keyframe 0 is for setup
    if keyframe == 0:
        leg.setAngles(512,512,512)
        
    elif keyframe == 1:
            leg.setAngles(608,837,196)     
    elif keyframe == 2:
            leg.setAngles(397,512,512)
            
def wave(keyframe,leg):
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
        
def waveInverse(keyframe,leg):
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

def twerk(keyframe, leg, angle):
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

def greet(keyframe,leg,angle):
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

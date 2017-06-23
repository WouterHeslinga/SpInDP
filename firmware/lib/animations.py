import leg2 as leg
import math as math
from time import sleep

def balloon(keyframe, leg):
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
        leg.changePos(130,0,110, add=False)

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
        leg.changePos(130,0,110, add=False, apply=False)

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
        pass

    elif keyframe == 1:
        leg.setAngles(512,204,512)
    elif keyframe == 2:
        leg.setAngles(512,204,305)
    elif keyframe == 3:
        leg.setAngles(512, 204,512)

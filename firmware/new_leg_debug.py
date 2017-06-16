import lib.servo as servo
import lib.leg2 as leg
from time import sleep
import math

def map_legs(servos):
    legs = []
    knees = {}
    hips = {}
    feet = {}
    for servo in servos:
        if servo.joint == "knee":
            knees[servo.leg] = servo
        elif servo.joint == "hip":
            hips[servo.leg] = servo
        elif servo.joint == "foot":
            feet[servo.leg] = servo

        if servo.leg in knees and servo.leg in hips and servo.leg in feet:
            legs.append(leg.Leg(servo.leg, hips[servo.leg], knees[servo.leg], feet[servo.leg]))
    return legs

def animation_balloon(keyframe, leg):
    stepWidth = 100
    
    # keyframe 0 is for setup
    if keyframe == 0:
        if leg.id == 3 or leg.id == 6:
            leg.setPos(stepWidth / 2, stepWidth / 2, 0, invertX=False)
        elif leg.id == 2 or leg.id == 5:
            leg.setPos(stepWidth / 2, -stepWidth / 2, 0, invertX=False)

    if keyframe == 1:
        if leg.id == 1 or leg.id == 4:
            leg.setPos(0, -stepWidth * 1.4, 250, offset=False)
    elif keyframe == 2:
        if leg.id == 1 or leg.id == 4:
            leg.setPos(0, stepWidth * 1.4, -250, offset=False)

def animation_rotate(keyframe, leg, direction):
    
def animation_walk(keyframe, leg, angle=0):
    stepWidth = 80
    stepHeight = 60
    radfactor = math.pi / 180
    stepWidthY = stepWidth * math.cos(angle * radfactor)
    stepWidthX = stepWidth * math.sin(angle * radfactor)
    
    # keyframe 0 is for setup
    if keyframe == 0:
        if leg.isEven():
            leg.setPos(-stepWidthX / 2, -stepWidthY / 2, 0)
            
        else:
            leg.setPos(stepWidthX / 2, stepWidthY / 2, 0)
        
    elif keyframe == 1:
        if leg.isEven():
            leg.setPos(stepWidthX / 2, stepWidthY / 2, 0)
        else:
            leg.setPos(-stepWidthX / 2, -stepWidthY / 2, stepHeight)
        
    elif keyframe == 2:
        if leg.isEven():
            leg.setPos(stepWidthX / 2, stepWidthY / 2, 0)
        else:
            leg.setPos(-stepWidthX / 2, -stepWidthY / 2, -stepHeight)
        
    elif keyframe == 3:
        if leg.isEven():
            leg.setPos(-stepWidthX / 2, -stepWidthY / 2, stepHeight)
        else:
            leg.setPos(stepWidthX / 2, stepWidthY / 2, 0)
        
    elif keyframe == 4:
        if leg.isEven():
            leg.setPos(-stepWidthX / 2, -stepWidthY / 2, -stepHeight)
        else:
            leg.setPos(stepWidthX / 2, stepWidthY / 2, 0)
    

def play_animation(animation, totalKeyframes, timeout = 0.2):
    # set legs to default position
    for leg in legs:
        leg.setPos(153,0,100, add=False)
        
    sleep(0.5)

    # set legs to start position
    for leg in legs:
        animation(0, leg)
        
    sleep(timeout)

    # play animation
    keyframeEven = totalKeyframes / totalKeyframes
    if totalKeyframes == 1:
        keyframeUneven = 1
    else:
        keyframeUneven = totalKeyframes / 2 + 1
        
    while True:
        for leg in legs:
            if leg.isEven:
                animation(keyframeEven, leg)
            else:
                animation(keyframeUneven, leg)

        keyframeEven += 1
        keyframeUneven += 1

        if keyframeEven > totalKeyframes:
            keyframeEven = 1
        if keyframeUneven > totalKeyframes:
            keyframeUneven = 1
        sleep(timeout)

if __name__ == "__main__":
    servos = servo.readServoMappings()
    legs = map_legs(servos)
    sleep(1)

    
    play_animation(animation = animation_balloon, totalKeyframes = 2, timeout = 0.5)    

    #play_animation(animation = animation_walk, totalKeyframes = 4, timeout = 0.2)    

    #walk_start(legs)
    #sleep(1)

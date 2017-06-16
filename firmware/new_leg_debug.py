import lib.servo as servo
import lib.leg2 as leg
import lib.animations as animation
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
    

def play_animation(animation, totalKeyframes, timeout = 0.2):
    # set legs to default position
    for leg in legs:
        leg.changePos(130,0,100, add=False)
        
    sleep(1)

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

    print(range(1,19))
    sleep(15)
    while True:
        try:
            play_animation(animation = animation.walk, totalKeyframes = 4, timeout = 0.15)
            #play_animation(animation = animation.rotate, totalKeyframes = 4, timeout = 0.1)
            #play_animation(animation = animation.balloon, totalKeyframes = 3, timeout = 0.5)
        except KeyboardInterrupt as ex:
            break

    #sleep(1)

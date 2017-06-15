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

def walk_start(legs):
    timeout = 0.2
    angle = 0
    stepWidth = 100
    radfactor = math.pi / 180
    stepWidthY = int((stepWidth / 2) * math.cos(angle * radfactor))
    stepWidthX = int((stepWidth / 2) * math.sin(angle * radfactor))
    stepHeight = 30

    
    for leg in legs:
        print("\n Set leg: " + str(leg.id))
        leg.setPos(130, 0, 90, add=False)
        sleep(1)
        if leg.id % 2 == 0:
            print("even")
            leg.setPos(-stepWidthX / 2, -stepWidthY / 2, 0)
        elif leg.id % 2 != 0:
            print("uneven")
            leg.setPos(stepWidthX / 2, stepWidthY / 2, 0)
            

if __name__ == "__main__":
    servos = servo.readServoMappings()
    legs = map_legs(servos)
    sleep(1)

    # set legs to start position
    for leg in legs:
        leg.setPos(130, 0, 100, add=False)
    sleep(1)

    walk_start(legs)
    #sleep(1)

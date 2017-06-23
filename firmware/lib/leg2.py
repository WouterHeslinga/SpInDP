from time import sleep
from kinematics import legIk
import math
import Queue

class Leg():
    def __init__(self, id, hip_servo, knee_servo, foot_servo):
        """The class for moving the servo's to the right position"""
        self.hip = hip_servo
        self.knee = knee_servo
        self.foot = foot_servo
        self.id = id
        self.x = 0
        self.y = 0
        self.z = 0

    def isEven(self):
        return self.id % 2 == 0

    def changePos(self, x, y, z, speed = -1, add=True, offset=True, invertX=True, apply=True):
        rollx = 0
        pitchy = 0
        yawz = 0
        if add == True and invertX == True:
            if self.id == 1 or self.id == 2 or self.id == 3:
                x *= -1
            
        if add:
            self.x += x
            self.y += y
            self.z -= z
        else:
            self.x = x
            self.y = y
            self.z = z
            
        """Sets the rotation of the servo's according to the x y z using kinematics"""
        degrees = legIk(values = [self.x, self.y, self.z], leg = self.id, rollx=rollx, pitchy=pitchy, yawz=yawz)

        # Offset the angles
        if offset and (self.id != 2 and self.id != 5):
            degrees[0] += (-153 if (self.id == 1 or self.id == 4) else 153)
        
        if apply:
            self.moveHip(int(degrees[0]), speed)
            sleep(0.001)
            self.moveKnee(int(degrees[1]), speed)
            sleep(0.001)
            self.moveFoot(int(degrees[2]), speed)
            sleep(0.001)

    def setAngles(self, coxa, femur, tibia, speed = -1, offset=True):
        degrees = [coxa, femur, tibia]

        #offset 
        if offset and (self.id != 2 and self.id != 5):
            degrees[0] += (-153 if (self.id == 1 or self.id == 4) else 153)

        self.moveHip(int(degrees[0]), speed)
        sleep(0.001)
        self.moveKnee(int(degrees[1]), speed)
        sleep(0.001)
        self.moveFoot(int(degrees[2]), speed)
        sleep(0.001)

                
    def moveHip(self, rotation, speed = -1):
        if speed == -1:
            self.hip.move(rotation)
        else:
            self.hip.move(rotation, speed)

    def moveKnee(self, rotation, speed = -1):
        if speed == -1:
            self.knee.move(rotation)
        else:
            self.knee.move(rotation, speed)

    def moveFoot(self, rotation, speed = -1):
        if speed == -1:
            self.foot.move(rotation)
        else:
            self.foot.move(rotation, speed)

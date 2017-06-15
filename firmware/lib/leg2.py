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

    def setPos(self, x, y, z, speed = -1, add=True, offset=True):
        if add:
            self.x += x
            self.y += y
            self.z -= z
        else:
            self.x = x
            self.y = y
            self.z = z
        print("x = %d, y = %d, z = %d" % (self.x, self.y, self.z))
        
        """Sets the rotation of the servo's according to the x y z using kinematics"""
        degrees = legIk(values = [self.x, self.y, self.z])

        # Offset the angles
        if offset and (self.id != 2 and self.id != 5):
            degrees[0] += (-153 if (self.id == 1 or self.id == 4) else 153)
        
        """self.hip.move(int(degrees[0]), speed)
        self.knee.move(int(degrees[1]), speed)
        self.foot.move(int(degrees[2]), speed)"""

        print(str(degrees[0]) + " " + str(degrees[1]) + " " + str(degrees[2]))
        self.moveHip(int(degrees[0]), 150)
        sleep(0.01)
        self.moveKnee(int(degrees[1]), 150)
        sleep(0.01)
        self.moveFoot(int(degrees[2]), 150)
        sleep(0.01)

                
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

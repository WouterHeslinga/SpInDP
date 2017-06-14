from time import sleep
import threading
import kinematicsTest as ik
import math
import Queue


class leg (threading.Thread):
    def __init__(self, id, hip, knee, foot, moveQueue):
        threading.Thread.__init__(self)
        self.id = id
        self.hip = hip
        self.knee = knee
        self.foot = foot
        self.moveQueue = moveQueue
        self.taskList = Queue.Queue(0)
        self.currentTask = "idle"
        self.stopSignal = False

        self.x = 130.19
        self.y = 0
        self.z = 74.90

    def run(self):
        while self.stopSignal == False:
            self.checkNewTask()
	
    def changePos(self,addX = None, addY = None, addZ = None, setX = None, setY = None, setZ = None):
        if addX != None:
            self.x += addX
        if addY != None:
            self.y += addY
        if addZ != None:
            self.z -= addZ

        if setX != None:
            self.x = setX
        if setY != None:
            self.y = setY
        if setZ != None:
            self.z = setZ
            
        #return [self.x, self.y, self.z]
        self.move(ik.legIk(values = [self.x, self.y, self.z]))

    #values expects an array with hipRot, kneeRot, footRot
    def move(self, values, speed = -1):
        legId = self.id

        acsOffset = 0
        if legId == 1 or legId == 4:
            acsOffset = -153
        elif legId == 2 or legId == 5:
            acsOffset = 0
        elif legId == 3 or legId == 6:
            acsOffset = 153
        values[0] += acsOffset
        
       
        self.moveQueue.put([self, int(values[0]), int(values[1]), int(values[2]), int(speed)])

    # check if a new task is available
    def checkNewTask(self):
        newTask = ""
        if self.taskList.empty() == False:
            newTask = self.taskList.get()
        else:
            return False
        
        # if the new task equals the current task continue doing the current task
        if newTask == self.currentTask:
            return False

        self.currentTask = newTask
        self.switchTask()
            
        return True
        

    # switch to a new task
    def switchTask(self):
        #self.resetPos(x = 130.19, y = 0, z = 100.90)
        self.changePos(setX = 130.19, setY = 0, setZ = 100.90)
        sleep(1)
        
        if str(self.currentTask) == "f":
            while self.checkNewTask() == False:
                self.walk()
        elif str(self.currentTask) == "b":
            while self.checkNewTask() == False:
                self.walkBackwards()
        elif str(self.currentTask) == "l":
            while self.checkNewTask() == False:
                self.walkLeft()
        elif str(self.currentTask)[:1] == "u":
            while self.checkNewTask() == False:
                self.walkUniversal(angle = int(str(self.currentTask)[1:]))
        elif str(self.currentTask) == "turn":
            while self.checkNewTask() == False:
                self.walkTurn()
        elif str(self.currentTask) == "place":
            while self.checkNewTask() == False:
                self.walkTurnInPlace()
        elif self.currentTask == "idle":
            while self.checkNewTask() == False:
                sleep(0.2)
                
            

    def walkUniversal(self, x = 130.19, y = 0, z = 100.90, angle = 0):
        timeout = 0.2
        stepWidth = 100
        radfactor = math.pi / 180
        stepWidthY = int((stepWidth / 2) * math.cos(angle * radfactor))
        stepWidthX = int((stepWidth / 2) * math.sin(angle * radfactor))
        stepHeight = 30

        #angle between 0 and 180 (right), angle between 180 and 360 (left)
        if (angle > 0 and angle < 180) or (angle > 180 and angle < 360):
            if self.id == 1 or self.id == 2 or self.id == 3:
                stepWidthX *= -1

        # even legs
        if self.id % 2 == 0:
            
            self.changePos(addX = -stepWidthX / 2, addY = -stepWidthY / 2)
            sleep(timeout)

            while self.checkNewTask() == False:
                #ground
                self.changePos(addX = stepWidthX / 2, addY = stepWidthY / 2)
                sleep(timeout)
                self.changePos(addX = stepWidthX / 2, addY = stepWidthY / 2)
                sleep(timeout)

                #air
                self.changePos(addX = -stepWidthX / 2, addY = -stepWidthY / 2, addZ = stepHeight)
                sleep(timeout)
                self.changePos(addX = -stepWidthX / 2, addY = -stepWidthY / 2, addZ = -stepHeight)
                sleep(timeout)
                
                 
        # uneven legs                   
        elif self.id % 2 != 0:
            
            self.changePos(addX = stepWidthX / 2, addY = stepWidthY / 2)
            sleep(timeout)
            
            while self.checkNewTask() == False:
                #air
                self.changePos(addX = -stepWidthX / 2, addY = -stepWidthY / 2, addZ = stepHeight)
                sleep(timeout)
                self.changePos(addX = -stepWidthX / 2, addY = -stepWidthY / 2, addZ = -stepHeight)
                sleep(timeout)

                #ground
                self.changePos(addX = stepWidthX / 2, addY = stepWidthY / 2)
                sleep(timeout)
                self.changePos(addX = stepWidthX / 2, addY = stepWidthY / 2)
                sleep(timeout)         
                

    def walkTurnInPlace(self,x = 120.19, y = 0, z = 100.90):
        timeout = 0.1
        stepWidth = 122
        stepHeight = 30
        #                    x    y    z
        #initial feet pos 130.19, 0, 74.90)
        self.changePos(setX = x, setY = y, setZ = z)
        sleep(1)

        #step 1: leg 3 and 4

        if self.id == 3:
            self.changePos(addY = -stepWidth/2, addZ = stepHeight)
        elif self.id == 4:
            self.changePos(addY = stepWidth/2, addZ = stepHeight)
        
        sleep(timeout)

        if self.id == 3 or self.id == 4:
            self.changePos(addZ = -stepHeight)
            
        sleep(timeout)

        #step 2: leg 1 and 6
        
        if self.id == 1:
            self.changePos(addY = -stepWidth/2, addZ = stepHeight)
        elif self.id == 6:
            self.changePos(addY = stepWidth/2, addZ = stepHeight)

        sleep(timeout)
        
        if self.id == 1 or self.id == 6:
            self.changePos(addZ = -stepHeight)

        sleep(timeout)

        #initialize loop

        while self.checkNewTask() == False:
            #step 3:leg 2 and 5 up
            if self.id == 2 or self.id == 5:
                self.changePos(addZ = stepHeight)
            sleep(timeout)
            
            #step 4: move legs 1,3,4,6 for the turn
            if self.id == 1 or self.id == 3:
                self.changePos(addY = stepWidth)
            elif self.id == 4 or self.id == 6:
                self.changePos(addY = -stepWidth)
            sleep(timeout)

            #step 5: leg 2 and 5 down again

            if self.id == 2 or self.id == 5:
                self.changePos(addZ = -stepHeight)
            sleep(timeout)

            #step 6: leg 3 and 4 on pos

            if self.id == 3:
                self.changePos(addY = -stepWidth, addZ = stepHeight)
            elif self.id == 4:
                self.changePos(addY = stepWidth, addZ = stepHeight)
        
            sleep(timeout)

            if self.id == 3 or self.id == 4:
                self.changePos(addZ = -stepHeight)

            #step 7: leg 1 and 6 on pos

            if self.id == 1:
                self.changePos(addY = -stepWidth, addZ = stepHeight)
            elif self.id == 6:
                self.changePos(addY = stepWidth, addZ = stepHeight)

            sleep(timeout)
        
            if self.id == 1 or self.id == 6:
                self.changePos(addZ = -stepHeight)

            sleep(timeout)

            #step 3 again
            
    def walkTurn(self,x = 120.19, y = 0, z = 100.90):
        timeout = 0.1
        stepWidth = -60
        stepHeight = 30
        #                    x    y    z
        #initial feet pos 130.19, 0, 74.90):
        self.changePos(setX = x, setY = y, setZ = z)
        
        sleep(1)

        # even legs
        if self.id == 2:
            
            self.changePos(addY = -stepWidth / 2)
            sleep(timeout)

            while self.checkNewTask() == False:
                
                self.changePos(addY = stepWidth / 2)
                sleep(timeout)

                self.changePos(addY = stepWidth / 2)
                sleep(timeout)
                 
                self.changePos(addY = -stepWidth, addZ = stepHeight)
                sleep(timeout)

                self.changePos(addZ = -stepHeight)
                sleep(timeout)

        elif self.id == 4 or self.id == 6:
            
            self.changePos(addY = stepWidth / 2)
            sleep(timeout)

            while self.checkNewTask() == False:
                
                self.changePos(addY = -stepWidth / 2)
                sleep(timeout)

                self.changePos(addY = -stepWidth / 2)
                sleep(timeout)
                 
                self.changePos(addY = stepWidth, addZ = stepHeight)
                sleep(timeout)

                self.changePos(addZ = -stepHeight)
                sleep(timeout)




        elif self.id == 1 or self.id == 3:
            
            self.changePos(addY = -stepWidth / 2)
            sleep(timeout)
            
            while self.checkNewTask() == False:
                
                self.changePos(addY = -stepWidth, addZ = stepHeight)
                sleep(timeout)
                
                self.changePos(addZ = -stepHeight)
                sleep(timeout)

                self.changePos(addY = stepWidth / 2)
                sleep(timeout)

                self.changePos(addY = stepWidth / 2)
                sleep(timeout)

        elif self.id == 5:
            
            self.changePos(addY = stepWidth / 2)
            sleep(timeout)
            
            while self.checkNewTask() == False:
                
                self.changePos(addY = stepWidth, addZ = stepHeight)
                sleep(timeout)
                
                self.changePos(addZ = -stepHeight)
                sleep(timeout)

                self.changePos(addY = -stepWidth / 2)
                sleep(timeout)

                self.changePos(addY = -stepWidth / 2)
                sleep(timeout)

    """def resetPos(self,x = 120.19, y = 0, z = 100.90):
        totalTimeout = 6
        timeout = int(totalTimeout - (self.id * totalTimeout))
        sleep(timeout)
        self.changePos(setX = x, setY = y, setZ = z -30)
        sleep(0.2)
        self.changePos(setX = x, setY = y, setZ = z + 30)
        remainingTimeout = int(totalTimeout - timeout)
        sleep(remainingTimeout)"""

        
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

        
           


                               

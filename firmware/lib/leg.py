from time import sleep
import threading
import kinematics as ik
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
        #self.walk(130.19,0,74.90)
        while self.stopSignal == False:
            self.checkNewTask()
	
    def changePos(self,addX = None, addY = None, addZ = None, setX = None, setY = None, setZ = None):
        if addX != None:
            self.x += addX
        if addY != None:
            self.y += addY
        if addZ != None:
            self.z += addZ

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
        if str(self.currentTask) == "f":
            while self.checkNewTask() == False:
                self.walk()
        elif str(self.currentTask) == "b":
            while self.checkNewTask() == False:
                self.walkBackwards()
        elif self.currentTask == "idle":
            while self.checkNewTask() == False:
                sleep(0.2)
                
            

        
    def walk(self,x = 130.19, y = 0, z = 74.90):
        timeout = 0.3
        #                    x    y    z
        #initial feet pos 130.19, 0, 74.90)
        self.changePos(setX = x, setY = y, setZ = z)
        sleep(1)

        # even legs
        if self.id % 2 == 0:
            
            self.changePos(addY = 27)
            sleep(timeout)

            while self.checkNewTask() == False:
                
                self.changePos(addY = -54)
                sleep(timeout)
                 
                self.changePos(addY = 54, addZ = 40)
                sleep(timeout)

                self.changePos(addZ = -40)
                sleep(timeout)

        # uneven legs                   
        elif self.id % 2 != 0:
            
            self.changePos(addY = -27)
            sleep(timeout)
            
            while self.checkNewTask() == False:
                
                self.changePos(addY = 54, addZ = 40)
                sleep(timeout)
    
                self.changePos(addZ = -40)
                sleep(timeout)

                self.changePos(addY = -54)
                sleep(timeout)


    def walkBackwards(self,x = 130.19, y = 0, z = 74.90):
        timeout = 0.3
        #                    x    y    z
        #initial feet pos 130.19, 0, 74.90):
        self.changePos(setX = x, setY = y, setZ = z)
        
        sleep(1)

        # even legs
        if self.id % 2 == 0:
            
            self.changePos(addY = -27)
            sleep(timeout)

            while self.checkNewTask() == False:
                
                self.changePos(addY = 54)
                sleep(timeout)
                 
                self.changePos(addY = -54, addZ = 40)
                sleep(timeout)

                self.changePos(addZ = -40)
                sleep(timeout)

        # uneven legs                   
        elif self.id % 2 != 0:
            
            self.changePos(addY = 27)
            sleep(timeout)
            
            while self.checkNewTask() == False:
                
                self.changePos(addY = -54, addZ = 40)
                sleep(timeout)
                
                self.changePos(addZ = -40)
                sleep(timeout)

                self.changePos(addY = 54)
                sleep(timeout)

                

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

        
           


                               

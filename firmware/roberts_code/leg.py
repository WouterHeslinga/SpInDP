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

    def run(self):
        #self.walk(130.19,0,74.90)
        while self.stopSignal == False:
            self.checkNewTask()
	
    def queueMove(self, hipRot = -1, kneeRot = -1, footRot = -1, speed = -1):
        self.moveQueue.put([self, hipRot, kneeRot, footRot, speed])

    #values expects an array with hipRot, kneeRot, footRot
    def move(self, values):
        legId = self.id

        acsOffset = 0
        if legId == 1 or legId == 4:
            acsOffset = -153
        elif legId == 2 or legId == 5:
            acsOffset = 0
        elif legId == 3 or legId == 6:
            acsOffset = 153
        values[0] += acsOffset
        
        self.queueMove(hipRot = int(values[0]), kneeRot = int(values[1]), footRot = int(values[2]))

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
        timeout = 0.2
        #                    x    y    z
        #initial feet pos 130.19, 0, 74.90
        startPos = [x,y,z]
        currentPos = startPos
        
        self.move(ik.legIk(startPos[0], startPos[1] , startPos[2]))
        
        sleep(0.7)
        
        if self.id % 2 == 0:
            y += 28
            self.move(ik.legIk(x, y, z))

            sleep(timeout)

            self.move(ik.legIk(x, y, z))

            while self.checkNewTask() == False:
                y -= 56
                self.move(ik.legIk(x, y, z))

                sleep(timeout)
                 
                y += 56
                z += 40
                self.move(ik.legIk(x, y, z))
                    
                sleep(timeout)

                z -= 40
                self.move(ik.legIk(x, y, z))
                sleep(timeout)

        #input = raw_input("2")
                   
        elif self.id % 2 != 0:
            
            y -= 28
            self.move(ik.legIk(x, y, z))

            sleep(timeout)

            self.move(ik.legIk(x, y, z))
            
            while self.checkNewTask() == False:
                y += 56
                z += 40
                self.move(ik.legIk(x, y, z))
    
                sleep(timeout)
    
                z -= 40
                self.move(ik.legIk(x, y, z))
                    
                sleep(timeout)

                y -= 56
                self.move(ik.legIk(x, y, z))

                sleep(timeout)


    def walkBackwards(self,x = 130.19, y = 0, z = 74.90):
        timeout = 0.2
        #                    x    y    z
        #initial feet pos 130.19, 0, 74.90
        startPos = [x,y,z]
        currentPos = startPos
        
        self.move(ik.legIk(startPos[0], startPos[1] , startPos[2]))
        
        sleep(0.7)
        
        if self.id % 2 == 0:
            y -= 28
            self.move(ik.legIk(x, y, z))

            sleep(timeout)

            self.move(ik.legIk(x, y, z))

            while self.checkNewTask() == False:
                y += 56
                self.move(ik.legIk(x, y, z))

                sleep(timeout)
                 
                y -= 56
                z += 40
                self.move(ik.legIk(x, y, z))
                    
                sleep(timeout)

                z -= 40
                self.move(ik.legIk(x, y, z))
                sleep(timeout)

        #input = raw_input("2")
                   
        elif self.id % 2 != 0:
            
            y += 28
            self.move(ik.legIk(x, y, z))

            sleep(timeout)

            self.move(ik.legIk(x, y, z))
            
            while self.checkNewTask() == False:
                y -= 56
                z += 40
                self.move(ik.legIk(x, y, z))
    
                sleep(timeout)
    
                z -= 40
                self.move(ik.legIk(x, y, z))
                    
                sleep(timeout)

                y += 56
                self.move(ik.legIk(x, y, z))

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
           


                               

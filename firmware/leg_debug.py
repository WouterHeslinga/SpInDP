#!/usr/bin/python3

import lib.connection as connection
import lib.debug as debug
import lib.debugKinematics as debugIk
import lib.leg as leg
import lib.servo as servo
import lib.kinematics as ik

import serial
import threading
import time
import math
from random import randint
import Queue


timeBetweenMovement = 1
timeBetweenSteps = 0.01

servos = []
legs = []

queue = Queue.Queue(0)

        
def main():
    global servos
    global legs
    global queue
    
    input = ""

    #read servo configuration from file
    servos = servo.readServoMappings()

    #fills legs[] with threads based on servos[]
    legs = mapLegs()
       
    
    activeThreads = []

    # Create serverThreads
    c_debugApp = connection.serverThread(7,"debugApp", legs, servos)
    c_controller = connection.serverThread(8,"controller", legs, servos)
    
    # Create debug threads
    debugWindow = debug.debugThread(9,"debugWindow", legs, servos)
    debugIkWindow = debugIk.debugThread(10,"debugIkWindow",legs,servos)

    # Create moveQueue thread
    queueHandler = queueHandlerThread(11,queue)
    queueHandler.start()
    activeThreads.append(queueHandler)

    time.sleep(1)

    while True:
        try:
            #getInput = "f"
            getInput = raw_input("\ndirections (f/b/l/r) d (rest/test) commands (c_c/c_d/debug/reread/remap/quit): ")
            if input != getInput:
                input = getInput
    
            if input == "test":
                setLegs(450,700,512)
            elif input == "rest":
                for leg in legs:
                    leg.taskList.put("idle")
                    
            elif input == "f":
                for leg in legs:
                    leg.taskList.put("f")
                    time.sleep(0.13)
                    
            
            elif input == "b":
                for leg in legs:
                    leg.taskList.put("b")
                    time.sleep(0.13)

            elif input == "torque":
                input = raw_input("torque: ")
                for x in servos:
                    x.setTorque(int(input))
            elif input == "c_d":
                if c_debugApp.isAlive() == False:
                    c_debugApp.start()
                    activeThreads.append(c_debugApp)
                else:
                    print("Already started")
                    

            elif input == "c_c":
                if c_controller.isAlive() == False:
                    c_controller.start()
                    activeThreads.append(c_controller)
                else:
                    print("Already started")

            elif input == "debug":
                if debugWindow.isAlive() == False:
                    debugWindow.start()
                else:
                    print("Window already open")

                
            elif input == "debugIk":
                if debugIkWindow.isAlive() == False:
                    debugIkWindow.start()
                    activeThreads.append(debugIkWindow)
                else:
                    print("Window already open")

            elif input == "move":
                if queueHandler.active == False:
                    queueHandler.set_active(True)
                else:
                    queueHandler.set_active(False)

            elif input == "reread":
                servos = servo.readServoMappings()
                legs = mapLegs()
            elif input == "remap":
                servo.mapServos()
                servo.readServoMappings()
            
            elif input == "quit":
                break

        except KeyboardInterrupt:
            print("\n")
            break
        except Exception as ex:
            print("Exception in main: " + str(ex))
            pass
        
        time.sleep(0.01)

    
    """if debugWindow.isAlive() == True:
        debugWindow.stop()

    if debugIkWindow.isAlive() == True:
        debugIkWindow.stop()
        
    for serverThread in activeServerThreads:
            serverThread.stop()"""

    for thread in activeThreads:
        if thread.isAlive():
            thread.stop()
            
    #wait for all threads to finish before shutdown
    for thread in activeThreads:
        if thread.isAlive():
            print("waiting for " + str(thread))
            thread.join()
            print("done " + str(thread))

def defaultPos():
    global legs

    for leg in legs:
        leg.move(ik.legIk(150,50,70))

def setAll(rotation):
    global servos
    for servo in servos:
        try:
            ax.ping(servo.id)
            servo.move(rotation)
        except:
            print("jammer")

def setLeg(legID,hip,knee,foot):
    global legs
    
    leg = legs[legID - 1] 
    leg.moveFoot(foot)
    leg.moveKnee(knee)
    leg.moveHip(hip)

def setLegs(hip,knee,foot):
    global legs

    for leg in legs:
        leg.moveFoot(foot)
        leg.moveKnee(knee)
        leg.moveHip(hip)

class queueHandlerThread(threading.Thread):
    def __init__(self, id, queue):
        threading.Thread.__init__(self)
        self.id = id
        self.queue = queue
        self.active = True
        self.stopSignal = False
    def set_active(self, state):
        if state == True:
            self.active = True
        if state == False:
            self.active = False
    def stop(self):
        self.active = False
        self.stopSignal = True
        
    def run(self):
        while self.stopSignal == False:                
            try:
                while self.active == False:
                    if self.stopSignal == True:
                        return
                    else:
                        time.sleep(1)
                    
                values = self.queue.get()
                
                leg = values[0]
                speed = values[4]
                if values[1] != -1:
                    leg.moveHip(int(values[1]),speed)
                if values[2] != -1:
                    leg.moveKnee(int(values[2]),speed)
                if values[3] != -1:
                    leg.moveFoot(int(values[3]),speed)

                time.sleep(0.01)
            except Exception as ex:
                print(str(ex))
        print("stopping")


def mapLegs():
    global servos
    legs = []
    
    print("\nSetting up legs")

    #6 legs
    for x in range (1,7):
            
        hip = -1
        knee = -1
        foot = -1
        
        count = 0
        for servo in servos:
                
            if x == int(servo.leg):
                try:
                    if servo.joint == "hip":
                        hip = count
                    elif servo.joint == "knee":
                        knee = count
                    elif servo.joint == "foot":
                        foot = count
                except:
                    print("assigning leg joint failed")

            count += 1

        if hip != -1 and knee != -1 and foot != -1:
            global queue
            newLeg = leg.leg(int(x), servos[hip], servos[knee], servos[foot], queue)
            newLeg.start()
            legs.append(newLeg)
            print("Leg ID: %s, hip: %s, knee: %s, foot: %s" % (str(x),legs[len(legs) - 1].hip.id, legs[len(legs) - 1].knee.id, legs[len(legs) - 1].foot.id))
        else:
            print("Leg ID: %s, hip: %s, knee: %s, foot: %s" % (str(x),-1,-1,-1))
								
    return legs

#execute main loop
if __name__ == '__main__':
    main()

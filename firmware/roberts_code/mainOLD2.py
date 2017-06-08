#!/usr/bin/python3

import connection as connection
import debug as debug
import debugKinematics as debugIk
import leg as leg
import servo as servo
import kinematics as ik

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
       
    
    # Create serverThreads
    c_debugApp = connection.serverThread(7,"debugApp", legs, servos)
    c_controller = connection.serverThread(8,"controller", legs, servos)
    activeServerThreads = []

    # Create debug thread
    debugWindow = debug.debugThread(9,"debugWindow", legs, servos)

    debugIkWindow = debugIk.debugThread(10,"debugIkWindow",legs,servos)

    # Create moveQueue thread
    queueHandler = queueHandlerThread(11,queue).start()

    time.sleep(1)

    while True:
        try:
            #getInput = "f"
            getInput = raw_input("\ndirections (f/b/l/r) d (rest/test) commands (c_c/c_d/debug/remap/quit): ")
            if input != getInput:
                input = getInput
    
            if input == "test":
                setLegs(450,700,512)
            if input == "rest":
                defaultPos()
                                    
            #front legs up
            if input == "preset1":
                preset1()

            #small
            if input == "preset2":
                setLegs(512,830,200)
                    
            if input == "f":
                #moveForward()

                for leg in legs:
                    leg.start()
                """while True:
                    try:
                        values = moveQueue.get()

                        print(values)

                        leg = values[0]
                        speed = values[4]
                        if values[1] != -1:
                            leg.moveHip(int(values[1]),speed)
                        if values[2] != -1:
                            leg.moveKnee(int(values[2]),speed)
                        if values[3] != -1:
                            leg.moveFoot(int(values[3]),speed)

                        #input = raw_input("x")
                        time.sleep(timeBetweenSteps)
                    except KeyboardInterrupt:
                        break"""
                    
                    
            if input == "b":
                moveBackward()

            if input == "c_d":
                c_debugApp.start()
                activeServerThreads.append(c_debugApp)
                    

            if input == "c_c":
                c_controller.start()
                activeServerThreads.append(c_controller)

            if input == "debug":
                debugWindow.start()

                
            if input == "debugIk":
                debugIkWindow.start()

            if input == "remap":
                servo.mapServos()
                servo.readServoMappings()
            
            if input == "quit":
                try:
                    debugWindow.stop()
                except Exception as ex:
                    print(str(ex))
                    
                for serverThread in activeServerThreads:
                        serverThread.stopServer()
                break

        except KeyboardInterrupt:
            print("\n")
            break
        except Exception as ex:
            print("Exception in main: " + str(ex))
            pass
        
        time.sleep(0.01)

    #wait for all threads to finish before shutdown
    for serverThread in activeServerThreads:
            serverThread.join()


        
def preset1():
    setLeg(1,600,715,340)
    setLeg(4,600,715,340)
    
    setLeg(2,700,250,750)
    setLeg(5,700,250,750)

    setLeg(3,512,250,750)
    setLeg(6,512,250,750)

def defaultPos():
    global legs

    time.sleep(3)
    for leg in legs:
        leg.move(ik.legIk(150,50,70))


def moveForward():
    global legs

    unevenLegs = [1,3,5]
    evenLegs = [2,4,6]
    for leg in legs:
        if leg.id in unevenLegs:
            moveLegForwardAir(leg)
        if leg.id in evenLegs:
            moveLegBackwardGround(leg)

    time.sleep(0.2)
    
    for leg in legs:
        moveLegToGround(leg)

    time.sleep(0.2)
    
    for leg in legs:
        if leg.id in unevenLegs:
            moveLegBackwardGround(leg)
        if leg.id in evenLegs:
            moveLegForwardAir(leg)

    time.sleep(0.2)
    
    for leg in legs:
        moveLegToGround(leg)

    time.sleep(0.2)


def moveBackward():
    global legs

    unevenLegs = [1,3,5]
    #leg 1 3 5
    for leg in legs:
        if leg.id in unevenLegs:
            moveLegBackwardAir(leg)

    evenLegs = [2,4,6]
    #leg 2 4 6
    for leg in legs:
        if leg.id in evenLegs:
            moveLegForwardGround(leg)
    time.sleep(0.3)
    
    #leg 1 3 5
    for leg in legs:
        if leg.id in unevenLegs:
            moveLegForwardGround(leg)
    
    #leg 2 4 6
    for leg in legs:
        if leg.id in evenLegs:
            moveLegBackwardAir(leg)
            
    time.sleep(0.3)


def moveLegForwardAir(leg):
    #foot up
    leg.moveFoot(400)
    #knee up
    leg.moveKnee(735)

    #hip forward
    leg.moveHip(576)
		
def moveLegBackwardAir(leg):
    #foot up
    leg.moveFoot(400)
    #knee up
    leg.moveKnee(735)

    #hip backward
    leg.moveHip(436)
		
def moveLegForwardGround(leg):
    #hip forward
    leg.moveHip(576)

def moveLegBackwardGround(leg):
    #hip backward
    leg.moveHip(436)
	
def moveLegToGround(leg):
    #foot down
    leg.moveFoot(340)
    #knee down
    leg.moveKnee(700)

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
    def set_active(self, state):
        if state == True:
            self.active = True
        if state == False:
            self.active = False

    def run(self):
        while True:            
            """while self.active == False:
                time.sleep(0.5)"""
                
            try:
                values = self.queue.get()

                print(values)

                leg = values[0]
                speed = values[4]
                if values[1] != -1:
                    leg.moveHip(int(values[1]),speed)
                if values[2] != -1:
                    leg.moveKnee(int(values[2]),speed)
                if values[3] != -1:
                    leg.moveFoot(int(values[3]),speed)

                #input = raw_input("x")
                time.sleep(0.01)
            except Exception as ex:
                print(str(ex))


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
main()

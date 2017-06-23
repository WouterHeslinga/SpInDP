import ax12
import RPi.GPIO as GPIO
from time import sleep

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

ax = ax12.Ax12()

class Servo():
    def __init__(self, id, side, leg, joint):
        self.id = id
        self.side = side
        self.leg = leg
        self.joint = joint
        self.temperature = 0
        self.angle = 0
        self.defaultSpeed = 850
    
    def getTemperature(self):
        self.temperature = ax.readTemperature(self.id)
        return self.temperature 
    
    def getAngle(self):
        self.angle = ax.readPosition(self.id)
        return self.angle

    def setTorque(self,value):
        ax.setTorqueLimit(self.id,value)
    
    def move(self, rotation, speed = -1):
        #clamp values
        if self.joint == "hip":
            if rotation < 340:
                rotation = 340

            elif rotation > 684:
                rotation = 684
        
        elif self.joint == "knee":
            if rotation < 175:
                rotation = 175

            elif rotation > 860:
                rotation = 860

        elif self.joint == "foot":
            if rotation < 175:
                rotation = 175

            elif rotation > 900:
                rotation = 900
            
        if speed == -1:
            speed = self.defaultSpeed
        try:
            if self.joint == "hip":
                if self.side == "r":
                    ax.moveSpeed(self.id, rotation, speed)
                elif self.side == "l":
                    ax.moveSpeed(self.id, (512 + 512 - rotation), speed) 
            else:
                ax.moveSpeed(self.id, rotation, speed) 
        except Exception as ex:
                print(str(ex))
    
    
    def toggleLight(self, status):
        ax.setLedStatus(self.id,status)	

def mapServos():
    servos = []
    
    mappingData = ""
    f = open('./config/mappingData', 'w')
    
    print("\nServo setup")
    #18 servo's
    for x in range (1,19):
        try:
            print "Pinging: " + str(x) + "... ",
            ax.ping(x)
            ax.setLedStatus(x,1)

            print "servo found, LED on "
            side = raw_input("Spider side (l,r): ")
            leg = raw_input("Spider leg (1..6): ")
            joint = raw_input("Spider joint group (hip,knee,foot): ")
            

            mappingData += "%s,%s,%s,%s,\n" % (x, side, leg, joint)
            servos.append(Servo(x,side,leg,joint))
            ax.setLedStatus(x,0)
            print("servo setup complete, LED off")
        except KeyboardInterrupt:
            mappingData += "%s,%s,%s,%s,\n" % (x, " "," "," ")
            ax.setLedStatus(x,0)
            print("setup of servo aborted")
        except:
            mappingData += "%s,%s,%s,%s,\n" % (x, " "," "," ")
            print("servo not found")

    print (mappingData)
    f.write(mappingData)
    f.close()

    return servos

def readServoMappings():
    servos = []
    f = open('./config/mappingData', 'r')

    print("\nSearching servo's")
    for x in range (1,19):
        try:			
            line = f.readline()
            print "Pinging: " + str(x) + "... ",
            sleep(.01)
            ax.ping(x)

            print "servo found... ",
            servoInfo = line.split(",") 
            side = servoInfo[1]
            leg = int(servoInfo[2])
            joint = servoInfo[3]
            print "ID: %s, Side: %s, Leg: %s, Joint: %s... " % (servoInfo[0], servoInfo[1], servoInfo[2], servoInfo[3]),
            
            servos.append(Servo(int(x),side,leg,joint))
            print("succes")
        except KeyboardInterrupt:
            print("failed")
        except:
            print("not found")

    f.close()

    return servos

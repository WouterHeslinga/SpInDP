import sched, time
import lib.servo as servo
#import lib.leg as leg
import threading
from time import sleep

servos = []
legs = []

def main():
	global servos
	global legs

	servos = servo.readServoMappings
	legs = mapLegs()

	while True:
		print("main")
		sleep(1)
	"""for leg in legs:
		leg = Dance(leg)
		print("1")
		dance.run()"""


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
            newLeg = leg(int(x))
            newLeg.start()
            legs.append(newLeg)
            print("Leg ID: %s, hip: %s, knee: %s, foot: %s" % (str(x),legs[len(legs) - 1].hip.id, legs[len(legs) - 1].knee.id, legs[len(legs) - 1].foot.id))
        else:
            print("Leg ID: %s, hip: %s, knee: %s, foot: %s" % (str(x),-1,-1,-1))
	
	return legs

class leg (threading.Thread):
    def __init__(self, id):
		threading.Thread.__init__(self)
		self.id = id
		self.x = 130.19
		self.y = 0
		self.z = 74.90

    def run(self):
		while True:
			print(str(self.id))
			sleep(1)

class Dance(threading.Thread):
	def __init__(self, leg):
		threading.Thread.__init__(self)
		self.s = sched.scheduler(time.time, time.sleep)
		self.leg = leg
		print("init")
	
	
	def run(self):
		while True:
			self.leg
		self.dance()


	def dance(self):
		print("dancing")
		leg = self.leg

		leg.setAngles(512,512,512)
		sleep(0.001)
		self.s.enter(0.01, 1, self.part1(leg), ())
		self.s.enter(3.3, 1, self.part2(leg), ())
		self.s.enter(14.5, 1, self.part3(leg), ())
		self.s.enter(37.2, 1, self.part4(leg), ())
		self.s.enter(57, 1, self.part5(leg), ())
		self.s.enter(77, 1, self.part6(leg), ())
		self.s.enter(95.54, 1, self.part7(leg), ())
		self.s.enter(111, 1, self.part8(leg), ())
		self.s.run()

	def part1(self, leg):
		if leg.id == 2:
			leg.setAngles(696,512,512)
		elif leg.id == 1:
			leg.setAngles(722,714,767)
		print("wave")
		sleep(0.5)
		if leg.id == 1:
			leg.setAngles(916,714,688)
		print("wave")
		sleep(0.5)
		if leg.id == 1:
			leg.setAngles(722,714,767)
		print("wave")
		sleep(0.5)
		if leg.id == 1:
			leg.setAngles(916,714,688)
		print("wave")
		sleep(0.5)
		if leg.id == 1:
			leg.setAngles(722,714,767)
		print("wave")
		sleep(0.5)
		if leg.id == 1:
			leg.setAngles(916,714,688)
		print("wave")
		sleep(0.5)

	def part2(self, leg):
		leg.setAngles(512,837,196,speed= 100)
		print("downslow")
		sleep(1.5)
		leg.setAngles(512,301,731)
		print("up")
		sleep(1.22)
		leg.setAngles(512,837,196)
		print("down")
		sleep(1.23)
		leg.setAngles(512,573,424)
		print("halfup")
		sleep(0.15)
		leg.setAngles(512,301,731)
		print("up")
		sleep(1.05)
		leg.setAngles(512,837,196)
		print("down")
		8.4
		sleep(1.2)
		leg.setAngles(512,301,731)
		print("up")
		sleep(1.2)
		leg.setAngles(512,837,196)
		print("down")
		sleep(1.2)
		leg.setAngles(512,573,424)
		print("halfup")
		sleep(0.15)
		leg.setAngles(512,301,731)
		print("up")

	def part3(self, leg):
		if leg.id == 1 or leg.id == 2 or leg.id == 3:
			leg.setAngles(512,433,556)
		elif leg.id == 4 or leg.id == 5 or leg.id == 6:
			leg.setAngles(512,609,547)
		print("to right")
		sleep(1.2)
		if leg.id == 1 or leg.id == 2 or leg.id == 3:
			leg.setAngles(512,609,547)
		elif leg.id == 4 or leg.id == 5 or leg.id == 6:
			leg.setAngles(512,433,556)
		print("to left")
		sleep(1.2)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("to front")
		sleep(0.15)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("to back")
		sleep(1.05)
		leg.setAngles(397,512,512)
		print("hipstoleft")
		sleep(1.2)
		if leg.id == 1 or leg.id == 2 or leg.id == 3:
			leg.setAngles(512,433,556)
		elif leg.id == 4 or leg.id == 5 or leg.id == 6:
			leg.setAngles(512,609,547)
		print("to right")
		sleep(1.2)
		if leg.id == 1 or leg.id == 2 or leg.id == 3:
			leg.setAngles(512,609,547)
		elif leg.id == 4 or leg.id == 5 or leg.id == 6:
			leg.setAngles(512,433,556)
		print("to left")
		sleep(1.2)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("to front")
		sleep(0.15)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("to back")
		sleep(1.05)
		leg.setAngles(608,837,196)
		print("hipstoright")
		sleep(1.2)
		if leg.id == 1 or leg.id == 2 or leg.id == 3:
			leg.setAngles(512,433,556)
		elif leg.id == 4 or leg.id == 5 or leg.id == 6:
			leg.setAngles(512,609,547)
		print("to right")
		sleep(1.2)
		if leg.id == 1 or leg.id == 2 or leg.id == 3:
			leg.setAngles(512,609,547)
		elif leg.id == 4 or leg.id == 5 or leg.id == 6:
			leg.setAngles(512,433,556)
		print("to left")
		sleep(1.2)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("to front")
		sleep(0.15)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("to back")
		sleep(1.05)
		leg.setAngles(397,512,512)
		print("hipstoleft")
		sleep(1.2)
		if leg.id == 1 or leg.id == 2 or leg.id == 3:
			leg.setAngles(512,433,556)
		elif leg.id == 4 or leg.id == 5 or leg.id == 6:
			leg.setAngles(512,609,547)
		print("to right")
		sleep(1.2)
		if leg.id == 1 or leg.id == 2 or leg.id == 3:
			leg.setAngles(512,609,547)
		elif leg.id == 4 or leg.id == 5 or leg.id == 6:
			leg.setAngles(512,433,556)
		print("to left")
		sleep(1.2)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("to front")
		sleep(0.15)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("to back")
		sleep(1.05)
		leg.setAngles(608,837,196)
		print("hipstoright")
		sleep(1.2)
		leg.setAngles(512,301,731, speed=100)
		print("up slow")

	def part4(self, leg):
		leg.setAngles(512,512,512)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("setup twerk")
		sleep(1.2)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,635,389, speed = 800)
		print("twerk down")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565, speed = 800)
		print("twerk up")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,635,389, speed = 800)
		print("twerk down")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565, speed = 800)
		print("twerk up")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,635,389, speed = 800)
		print("twerk down")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565, speed = 800)
		print("twerk up")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,635,389, speed = 800)
		print("twerk down")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565, speed = 800)
		print("twerk up")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,635,389, speed = 800)
		print("twerk down")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565, speed = 800)
		print("twerk up")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,635,389, speed = 800)
		print("twerk down")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565, speed = 800)
		print("twerk up")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,635,389, speed = 800)
		print("twerk down")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565, speed = 800)
		print("twerk up")
		sleep(0.3)
		if leg.id == 3 or leg.id == 6:
			leg.setAngles(512,635,389, speed = 800)
		print("twerk down")
		sleep(0.3)
		leg.setAngles(512,512,512, speed = 800)
		print("reset")
		sleep(0.3)
		print("43.2")
		leg.setAngles(608,837,196)
		print("hips left")
		sleep(0.3)
		leg.setAngles(397,512,512)
		print("hips right")
		sleep(0.3)
		leg.setAngles(608,837,196)
		print("hips left")
		sleep(0.3)
		leg.setAngles(397,512,512)
		print("hips right")
		sleep(0.3)
		leg.setAngles(608,837,196)
		print("hips left")
		sleep(0.3)
		leg.setAngles(397,512,512)
		print("hips right")
		sleep(0.3)
		leg.setAngles(608,837,196)
		print("hips left")
		sleep(0.3)
		leg.setAngles(397,512,512)
		print("hips right")
		sleep(0.3)
		leg.setAngles(608,837,196)
		print("hips left")
		sleep(0.3)
		leg.setAngles(397,512,512)
		print("hips right")
		sleep(0.3)
		leg.setAngles(608,837,196)
		print("hips left")
		sleep(0.3)
		leg.setAngles(397,512,512)
		print("hips right")
		sleep(0.3)
		leg.setAngles(608,837,196)
		print("hips left")
		sleep(0.3)
		leg.setAngles(397,512,512)
		print("hips right")
		sleep(0.3)
		leg.setAngles(608,837,196)
		print("hips left")
		sleep(0.3)
		leg.setAngles(397,512,512)
		print("hips right")
		sleep(0.3)
		print("48")
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("wave1")
		sleep(0.3)
		leg.setAngles(512,459,565)
		print("wave2")
		sleep(0.3)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("wave3")
		sleep(0.3)
		leg.setAngles(512,775,257)
		print("wave4")
		sleep(0.3)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("wave1")
		sleep(0.3)
		leg.setAngles(512,459,565)
		print("wave2")
		sleep(0.3)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("wave3")
		sleep(0.3)
		leg.setAngles(512,775,257)
		print("wave4")
		sleep(0.3)        
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("wave1")
		sleep(0.3)
		leg.setAngles(512,459,565)
		print("wave2")
		sleep(0.3)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("wave3")
		sleep(0.3)
		leg.setAngles(512,775,257)
		print("wave4")
		sleep(0.3)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("wave1")
		sleep(0.3)
		leg.setAngles(512,459,565)
		print("wave2")
		sleep(0.3)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("wave3")
		sleep(0.3)
		leg.setAngles(512,775,257)
		print("wave4")
		sleep(0.3)
		print("52.8")
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("inverse wave1")
		sleep(0.3)
		leg.setAngles(512,775,257)
		print("inverse wave2")
		sleep(0.3)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("inverse wave3")
		sleep(0.3)
		leg.setAngles(512,459,565)
		print("inverse wave4")
		sleep(0.3)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("inverse wave1")
		sleep(0.3)
		leg.setAngles(512,775,257)
		print("inverse wave2")
		sleep(0.3)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("inverse wave3")
		sleep(0.3)
		leg.setAngles(512,459,565)
		print("inverse wave4")
		sleep(0.3)
		print("55,2")
		leg.setAngles(512,512,512, speed = 600)

	def part5(self, leg):
		sleep(0.6)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.6)
		leg.setAngles(512,837,196)
		print("down")
		sleep(0.9)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.3)
		leg.setAngles(512,837,196)
		print("down")
		sleep(1.2)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.9)
		leg.setAngles(512,837,196)
		print("down")
		sleep(0.6)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.9)
		leg.setAngles(512,837,196)
		print("down")
		sleep(0.9)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.3)
		leg.setAngles(512,837,196)
		print("down")
		sleep(1.2)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.9)
		leg.setAngles(512,837,196)
		print("down")
		sleep(0.6)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.9)
		leg.setAngles(512,837,196)
		print("down")
		sleep(0.9)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.3)
		leg.setAngles(512,837,196)
		print("down")
		sleep(1.2)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.9)
		leg.setAngles(512,837,196)
		print("down")
		sleep(0.6)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.9)
		leg.setAngles(512,837,196)
		print("down")
		sleep(0.9)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.3)
		leg.setAngles(512,837,196)
		print("down")
		sleep(1.2)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.9)
		leg.setAngles(512,837,196)
		print("down")
		sleep(0.6)
		leg.setAngles(512,301,731)
		print("up")
		sleep(0.9)

	def part6(self, leg):
		leg.setAngles(512,512,512, speed = 200)
		print("set up fly")
		sleep(1.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		leg.setAngles(512,819,538, speed = 300)
		print("fly1")
		sleep(0.5)
		leg.setAngles(512,819,380, speed = 300)
		print("fly2")
		sleep(0.5)
		print("34.5")
		leg.setAngles(512,512,512, speed = 400)
		print("reset legs")

	def part7(self, leg):
		stepWidth = 54
		stepHeight = 30

		if leg.id == 2:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
		print("rotate0")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, -stepWidth, stepHeight, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, stepWidth, stepHeight, offset=False)
		print("rotate1")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, 0, -stepHeight, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, 0, -stepHeight, offset=False)
		print("rotate2")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, -stepWidth, stepHeight)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, stepWidth, stepHeight, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
		print("rotate3")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, 0, -stepHeight, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, 0, -stepHeight, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
		print("rotate4")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, -stepWidth, stepHeight, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, stepWidth, stepHeight, offset=False)
		print("rotate1")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, 0, -stepHeight, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, 0, -stepHeight, offset=False)
		print("rotate2")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, -stepWidth, stepHeight)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, stepWidth, stepHeight, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
		print("rotate3")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, 0, -stepHeight, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, 0, -stepHeight, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
		print("rotate4")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, -stepWidth, stepHeight, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, stepWidth, stepHeight, offset=False)
		print("rotate1")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, 0, -stepHeight, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, 0, -stepHeight, offset=False)
		print("rotate2")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, -stepWidth, stepHeight)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, stepWidth, stepHeight, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
		print("rotate3")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, 0, -stepHeight, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, 0, -stepHeight, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
		print("rotate4")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, -stepWidth, stepHeight, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, stepWidth, stepHeight, offset=False)
		print("rotate1")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, 0, -stepHeight, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, 0, -stepHeight, offset=False)
		print("rotate2")
		sleep(0.5)
		if leg.id == 2:
			leg.changePos(0, -stepWidth, stepHeight)
			
		elif leg.id == 4 or leg.id == 6:
			leg.changePos(0, stepWidth, stepHeight, offset=False)
			
		elif leg.id == 1 or leg.id == 3:
			leg.changePos(0, stepWidth / 2, 0, offset=False)
			
		elif leg.id == 5:
			leg.changePos(0, -stepWidth / 2, 0, offset=False)
		print("rotate3")
		sleep(0.5)
		print("1:43")
		leg.setAngles(512,512,512)
		print("reset angles")
		sleep(0.5)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("wave1")
		sleep(0.5)
		leg.setAngles(512,459,565)
		print("wave2")
		sleep(0.5)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("wave3")
		sleep(0.5)
		leg.setAngles(512,775,257)
		print("wave4")
		sleep(0.5)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("wave1")
		sleep(0.5)
		leg.setAngles(512,459,565)
		print("wave2")
		sleep(0.5)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("wave3")
		sleep(0.5)
		leg.setAngles(512,775,257)
		print("wave4")
		sleep(0.5)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("wave1")
		sleep(0.5)
		leg.setAngles(512,459,565)
		print("wave2")
		sleep(0.5)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("wave3")
		sleep(0.5)
		leg.setAngles(512,775,257)
		print("wave4")
		sleep(0.5)
		leg.setAngles(512,512,512, speed = 400)
		print("reset")

	def part8(self, leg):
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,775,257)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,459,565)
		print("fronttoback1")
		sleep(1)
		if leg.id == 1 or leg.id == 4:
			leg.setAngles(512,459,565)
		elif leg.id == 2 or leg.id == 5:
			leg.setAngles(512,635,389)
		elif leg.id == 3 or leg.id == 6:
			leg.setAngles(512,775,257)
		print("fronttoback2")
		sleep(1)
		leg.setAngles(512,512,512)
		print("reset")
		sleep(1)
		if leg.id == 1 or leg.id == 2 or leg.id == 3:
			leg.setAngles(512,433,556)
		elif leg.id == 4 or leg.id == 5 or leg.id == 6:
			leg.setAngles(512,609,547)
		print("righttoleft1")
		sleep(1)
		if leg.id == 1 or leg.id == 2 or leg.id == 3:
			leg.setAngles(512,609,547)
		elif leg.id == 4 or leg.id == 5 or leg.id == 6:
			leg.setAngles(512,433,556)
		print("righttoleft2")
		sleep(1)
		leg.setAngles(512,301,731)
		print("up")
		sleep(1.5)
		leg.setAngles(512,503,731)
		print("crash")

main()
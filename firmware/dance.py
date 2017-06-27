import sched, time
#import leg2 as leg
from time import sleep

s = sched.scheduler(time.time, time.sleep)
def dance():
	 #leg.setAngles(512,512,512)
	 s.enter(0.01, 1 , part1)
	 s.enter(3.3, 1, part2)
	 s.enter(14.5, 1, part3)
	 s.enter(37.2, 1, part4)
	 s.enter(57, 1, part5)
	 s.enter(77, 1, part6)
	 s.enter(95.54, 1, part7)
	 s.enter(111, 1, part8)
	 s.run()
def part1():
	#if leg.id == 2:
	    #leg.setAngles(696,512,512)
	#elif leg.id == 1:
	    #leg.setAngles(722,714,767)
	print("wave")
	sleep(0.5)
	#if leg.id == 1:
	    #leg.setAngles(916,714,688)
	print("wave")
	sleep(0.5)
	#if leg.id == 1:
	    #leg.setAngles(722,714,767)
	print("wave")
	sleep(0.5)
	#if leg.id == 1:
	    #leg.setAngles(916,714,688)
	print("wave")
	sleep(0.5)
	#if leg.id == 1:
	    #leg.setAngles(722,714,767)
	print("wave")
	sleep(0.5)
	#if leg.id == 1:
	    #leg.setAngles(916,714,688)
	print("wave")
	sleep(0.5)
def part2():
	#leg.setAngles(512,837,196,speed= 100)
	print("downslow")
	sleep(1.5)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(1.22)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(1.23)
	#leg.setAngles(512,573,424)
	print("halfup")
	sleep(0.15)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(1.05)
	#leg.setAngles(512,837,196)
	print("down")
	#8.4
	sleep(1.2)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(1.2)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(1.2)
	#leg.setAngles(512,573,424)
	print("halfup")
	sleep(0.15)
	#leg.setAngles(512,301,731)
	print("up")
def part3():
	#if leg.id == 1 or leg.id == 2 or leg.id == 3:
	#    leg.setAngles(512,433,556)
	#elif leg.id == 4 or leg.id == 5 or leg.id == 6:
	#    leg.setAngles(512,609,547)
	print("to right")
	sleep(1.2)
	#if leg.id == 1 or leg.id == 2 or leg.id == 3:
	#    leg.setAngles(512,609,547)
	#elif leg.id == 4 or leg.id == 5 or leg.id == 6:
	#    leg.setAngles(512,433,556)
	print("to left")
	sleep(1.2)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("to front")
	sleep(0.15)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("to back")
	sleep(1.05)
	#leg.setAngles(397,512,512)
	print("hipstoleft")
	sleep(1.2)
		#if leg.id == 1 or leg.id == 2 or leg.id == 3:
	#    leg.setAngles(512,433,556)
	#elif leg.id == 4 or leg.id == 5 or leg.id == 6:
	#    leg.setAngles(512,609,547)
	print("to right")
	sleep(1.2)
	#if leg.id == 1 or leg.id == 2 or leg.id == 3:
	#    leg.setAngles(512,609,547)
	#elif leg.id == 4 or leg.id == 5 or leg.id == 6:
	#    leg.setAngles(512,433,556)
	print("to left")
	sleep(1.2)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("to front")
	sleep(0.15)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("to back")
	sleep(1.05)
	#leg.setAngles(608,837,196)
	print("hipstoright")
	sleep(1.2)
	#if leg.id == 1 or leg.id == 2 or leg.id == 3:
	#    leg.setAngles(512,433,556)
	#elif leg.id == 4 or leg.id == 5 or leg.id == 6:
	#    leg.setAngles(512,609,547)
	print("to right")
	sleep(1.2)
	#if leg.id == 1 or leg.id == 2 or leg.id == 3:
	#    leg.setAngles(512,609,547)
	#elif leg.id == 4 or leg.id == 5 or leg.id == 6:
	#    leg.setAngles(512,433,556)
	print("to left")
	sleep(1.2)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("to front")
	sleep(0.15)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("to back")
	sleep(1.05)
	#leg.setAngles(397,512,512)
	print("hipstoleft")
	sleep(1.2)
		#if leg.id == 1 or leg.id == 2 or leg.id == 3:
	#    leg.setAngles(512,433,556)
	#elif leg.id == 4 or leg.id == 5 or leg.id == 6:
	#    leg.setAngles(512,609,547)
	print("to right")
	sleep(1.2)
	#if leg.id == 1 or leg.id == 2 or leg.id == 3:
	#    leg.setAngles(512,609,547)
	#elif leg.id == 4 or leg.id == 5 or leg.id == 6:
	#    leg.setAngles(512,433,556)
	print("to left")
	sleep(1.2)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("to front")
	sleep(0.15)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("to back")
	sleep(1.05)
	#leg.setAngles(608,837,196)
	print("hipstoright")
	sleep(1.2)
	#leg.setAngles(512,301,731, speed=100)
	print("up slow")
def part4():
	#leg.setAngles(512,512,512)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("setup twerk")
	sleep(1.2)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,635,389, speed = 800)
	print("twerk down")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565, speed = 800)
	print("twerk up")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,635,389, speed = 800)
	print("twerk down")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565, speed = 800)
	print("twerk up")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,635,389, speed = 800)
	print("twerk down")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565, speed = 800)
	print("twerk up")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,635,389, speed = 800)
	print("twerk down")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565, speed = 800)
	print("twerk up")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,635,389, speed = 800)
	print("twerk down")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565, speed = 800)
	print("twerk up")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,635,389, speed = 800)
	print("twerk down")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565, speed = 800)
	print("twerk up")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,635,389, speed = 800)
	print("twerk down")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565, speed = 800)
	print("twerk up")
	sleep(0.3)
	#if leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,635,389, speed = 800)
	print("twerk down")
	sleep(0.3)
	#    leg.setAngles(512,512,512, speed = 800)
	print("reset")
	sleep(0.3)
	print("43.2")
	#leg.setAngles(608,837,196)
	print("hips left")
	sleep(0.3)
	#leg.setAngles(397,512,512)
	print("hips right")
	sleep(0.3)
	#leg.setAngles(608,837,196)
	print("hips left")
	sleep(0.3)
	#leg.setAngles(397,512,512)
	print("hips right")
	sleep(0.3)
	#leg.setAngles(608,837,196)
	print("hips left")
	sleep(0.3)
	#leg.setAngles(397,512,512)
	print("hips right")
	sleep(0.3)
	#leg.setAngles(608,837,196)
	print("hips left")
	sleep(0.3)
	#leg.setAngles(397,512,512)
	print("hips right")
	sleep(0.3)
	#leg.setAngles(608,837,196)
	print("hips left")
	sleep(0.3)
	#leg.setAngles(397,512,512)
	print("hips right")
	sleep(0.3)
	#leg.setAngles(608,837,196)
	print("hips left")
	sleep(0.3)
	#leg.setAngles(397,512,512)
	print("hips right")
	sleep(0.3)
	#leg.setAngles(608,837,196)
	print("hips left")
	sleep(0.3)
	#leg.setAngles(397,512,512)
	print("hips right")
	sleep(0.3)
	#leg.setAngles(608,837,196)
	print("hips left")
	sleep(0.3)
	#leg.setAngles(397,512,512)
	print("hips right")
	sleep(0.3)
	print("48")
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("wave1")
	sleep(0.3)
	#leg.setAngles(512,459,565)
	print("wave2")
	sleep(0.3)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("wave3")
	sleep(0.3)
	#leg.setAngles(512,775,257)
	print("wave4")
	sleep(0.3)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("wave1")
	sleep(0.3)
	#leg.setAngles(512,459,565)
	print("wave2")
	sleep(0.3)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("wave3")
	sleep(0.3)
	#leg.setAngles(512,775,257)
	print("wave4")
	sleep(0.3)        
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("wave1")
	sleep(0.3)
	#leg.setAngles(512,459,565)
	print("wave2")
	sleep(0.3)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("wave3")
	sleep(0.3)
	#leg.setAngles(512,775,257)
	print("wave4")
	sleep(0.3)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("wave1")
	sleep(0.3)
	#leg.setAngles(512,459,565)
	print("wave2")
	sleep(0.3)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("wave3")
	sleep(0.3)
	#leg.setAngles(512,775,257)
	print("wave4")
	sleep(0.3)
	print("52.8")
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("inverse wave1")
	sleep(0.3)
	#leg.setAngles(512,775,257)
	print("inverse wave2")
	sleep(0.3)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("inverse wave3")
	sleep(0.3)
	#leg.setAngles(512,459,565)
	print("inverse wave4")
	sleep(0.3)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("inverse wave1")
	sleep(0.3)
	#leg.setAngles(512,775,257)
	print("inverse wave2")
	sleep(0.3)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("inverse wave3")
	sleep(0.3)
	#leg.setAngles(512,459,565)
	print("inverse wave4")
	sleep(0.3)
	print("55,2")
	#leg.setAngles(512,512,512, speed = 600)
def part5():
	sleep(0.6)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.6)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(0.9)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.3)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(1.2)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.9)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(0.6)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.9)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(0.9)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.3)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(1.2)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.9)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(0.6)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.9)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(0.9)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.3)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(1.2)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.9)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(0.6)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.9)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(0.9)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.3)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(1.2)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.9)
	#leg.setAngles(512,837,196)
	print("down")
	sleep(0.6)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(0.9)
def part6():
	#leg.setAngles(512,512,512, speed = 200)
	print("set up fly")
	sleep(1.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	#leg.setAngles(512,819,538, speed = 300)
	print("fly1")
	sleep(0.5)
	#leg.setAngles(512,819,380, speed = 300)
	print("fly2")
	sleep(0.5)
	print("34.5")
	#leg.setAngles(512,512,512, speed = 400)
	print("reset legs")
def part7():
	stepWidth = 54
	stepHeight = 30

	#if leg.id == 2:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	print("rotate0")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, -stepWidth, stepHeight, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, stepWidth, stepHeight, offset=False)
	print("rotate1")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	print("rotate2")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, -stepWidth, stepHeight)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, stepWidth, stepHeight, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	print("rotate3")
	sleep(0.5)
	#if leg.id == 2:
	#   leg.changePos(0, 0, -stepHeight, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	print("rotate4")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, -stepWidth, stepHeight, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, stepWidth, stepHeight, offset=False)
	print("rotate1")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	print("rotate2")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, -stepWidth, stepHeight)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, stepWidth, stepHeight, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	print("rotate3")
	sleep(0.5)
	#if leg.id == 2:
	#   leg.changePos(0, 0, -stepHeight, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	print("rotate4")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, -stepWidth, stepHeight, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, stepWidth, stepHeight, offset=False)
	print("rotate1")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	print("rotate2")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, -stepWidth, stepHeight)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, stepWidth, stepHeight, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	print("rotate3")
	sleep(0.5)
	#if leg.id == 2:
	#   leg.changePos(0, 0, -stepHeight, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	print("rotate4")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, -stepWidth, stepHeight, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, stepWidth, stepHeight, offset=False)
	print("rotate1")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, 0, -stepHeight, offset=False)
	print("rotate2")
	sleep(0.5)
	#if leg.id == 2:
	#    leg.changePos(0, -stepWidth, stepHeight)
	#    
	#elif leg.id == 4 or leg.id == 6:
	#    leg.changePos(0, stepWidth, stepHeight, offset=False)
	#    
	#elif leg.id == 1 or leg.id == 3:
	#    leg.changePos(0, stepWidth / 2, 0, offset=False)
	#    
	#elif leg.id == 5:
	#    leg.changePos(0, -stepWidth / 2, 0, offset=False)
	print("rotate3")
	sleep(0.5)
	print("1:43")
	#leg.setAngles(512,512,512)
	print("reset angles")
	sleep(0.5)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("wave1")
	sleep(0.5)
	#leg.setAngles(512,459,565)
	print("wave2")
	sleep(0.5)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#   leg.setAngles(512,459,565)
	print("wave3")
	sleep(0.5)
	#leg.setAngles(512,775,257)
	print("wave4")
	sleep(0.5)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("wave1")
	sleep(0.5)
	#leg.setAngles(512,459,565)
	print("wave2")
	sleep(0.5)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#   leg.setAngles(512,459,565)
	print("wave3")
	sleep(0.5)
	#leg.setAngles(512,775,257)
	print("wave4")
	sleep(0.5)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("wave1")
	sleep(0.5)
	#leg.setAngles(512,459,565)
	print("wave2")
	sleep(0.5)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#   leg.setAngles(512,459,565)
	print("wave3")
	sleep(0.5)
	#leg.setAngles(512,775,257)
	print("wave4")
	sleep(0.5)
	#leg.setAngles(512,512,512, speed = 400)
	print("reset")
def part8():
	#elif keyframe == 1:
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,775,257)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,459,565)
	print("fronttoback1")
	sleep(1)
	#if leg.id == 1 or leg.id == 4:
	#    leg.setAngles(512,459,565)
	#elif leg.id == 2 or leg.id == 5:
	#    leg.setAngles(512,635,389)
	#elif leg.id == 3 or leg.id == 6:
	#    leg.setAngles(512,775,257)
	print("fronttoback2")
	sleep(1)
	#leg.setAngles(512,512,512)
	print("reset")
	sleep(1)
	#if leg.id == 1 or leg.id == 2 or leg.id == 3:
	#    leg.setAngles(512,433,556)
	#elif leg.id == 4 or leg.id == 5 or leg.id == 6:
	#    leg.setAngles(512,609,547)
	print("righttoleft1")
	sleep(1)
	#if leg.id == 1 or leg.id == 2 or leg.id == 3:
	#    leg.setAngles(512,609,547)
	#elif leg.id == 4 or leg.id == 5 or leg.id == 6:
	#    leg.setAngles(512,433,556)
	print("righttoleft2")
	sleep(1)
	#leg.setAngles(512,301,731)
	print("up")
	sleep(1.5)
	#leg.setAngles(512,503,731)
	print("crash")
	

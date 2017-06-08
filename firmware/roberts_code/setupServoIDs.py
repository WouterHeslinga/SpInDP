import RPi.GPIO as GPIO
import ax12 as ax12
from random import randint

pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
#GPIO.setup(pin, GPIO.LOW)

ax = ax12.Ax12()

do = " "
while do != "quit":
	do = raw_input("Scan for servo's(s) || Bind servo(b): ")

	if do == "s":
		try:
			ax.learnServos(0,20,True)
		except:
			print("No servo's found")

	elif do == "b":
		try:
			oldID = raw_input("Select servo ID: ")
			newID = raw_input("New ID: ")
		
			ax.setID(int(oldID),int(newID))
		except:
			print("could not bind servo to new ID")
	elif do == "move":
		try:
			ax.moveSpeed(1,512,150)
		except:
			print("failed")
	
	#ax.setID(1,15)
	#ax.move(4,randint(500,520))
	#ax.move(5,randint(500,520))
	#ax.move(6,randint(500,520))
	

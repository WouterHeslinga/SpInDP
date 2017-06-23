#!/usr/bin/python3

from time import sleep
import math

def legIk(x = 0, y = 0, z = 0, values = None, leg = -1,rollx = 0, pitchy = 0, yawz = 0):
	if values != None:
		x = values[0]
		y = values[1]
		z = values[2]


	#legIk(130.19, 0, 74.90)
	#servo omhoog is 512+, servo naar rechts is -
	#feetpos
	#posX = 130.12
	#posY = 0

	bodyikfactor = 0.75
	if pitchy != 0:
		if leg == 1 or leg == 2 or leg == 3:
			z = z + (bodyikfactor * pitchy)
		if leg == 4 or leg == 5 or leg == 6:
			z = z - (bodyikfactor * pitchy)
	if rollx > 0:
		if leg == 1 or leg == 4:
			z = z + (bodyikfactor * rollx)
		if leg == 2 or leg == 5:
			z = z + ((bodyikfactor * rollx) * 0.5)
	if rollx < 0:
		if leg == 3 or leg == 6:
			z = z - (bodyikfactor * rollx)
		if leg == 2 or leg == 5:
			z = z - ((bodyikfactor * rollx) * 0.5)

	if yawz != 0:
                if leg == 1 or leg == 2 or leg == 3:
                        y = y + (bodyikfactor * yawz)
                if leg == 4 or leg == 5 or leg == 6:
                        y = y - (bodyikfactor * yawz)
                
  
	pifactor = 180 / math.pi
	radfactor = math.pi / 180

	e = z
	f = 37
	a = 67.19
	c = 145.11

	l = x
	coxaalphamax = 54
	coxaalphamaxhalf = (0.5 * coxaalphamax )* radfactor
	if (x != 0):
		ac = math.atan(float(y)/float(x)) * pifactor
	else:
		ac = math.atan(float(y)) * pifactor


	smallestl = math.cos(coxaalphamaxhalf) * l

	totalstep = 2 * math.sqrt(math.pow(l,2) - math.pow(smallestl,2))

	laccent = smallestl / (math.cos(ac * radfactor))

	d = laccent - f

	b = math.sqrt(math.pow(d,2) + math.pow(e,2))

	#alpha
	value = ((math.pow(a,2) - math.pow(c,2) - math.pow(b,2))/(-2 * c * b))
	if value > 1: value = 1 
	if value < -1: value = -1
	alpha = (math.acos(value) * pifactor)

	#gamma
	value = ((math.pow(c,2) - math.pow(b,2) - math.pow(a,2))/(-2 * b * a))
	if value > 1: value = 1 
	if value < -1: value = -1
	gamma = (math.acos(value)) * pifactor

	#beta
	value = (math.pow(b,2) - math.pow(a,2) - math.pow(c,2))/(-2 * a * c)
	if value > 1: value = 1 
	if value < -1: value = -1
	beta = (math.acos(value)) * pifactor


	if e != 0:
		delta = math.atan(float(d)/float(e)) * pifactor
	else:
		delta = math.atan(float(d)) * pifactor

	if d != 0:
		epsilon = math.atan(float(e)/float(d)) * pifactor
	else:
		epsilon = math.atan(float(e)) * pifactor

	alphaepsilon = alpha + epsilon


	af = (gamma - epsilon) + 14

	at = 121.1 - beta

	sfactor = 1024.00/300

	acs = (1024 - ((ac + 150) * sfactor))
	afs = (af + 150) * sfactor
	ats = (150 - at) * sfactor
  
	if leg == -1:
		print "Pos: [%d,%d,%d]" % (x,y,z),
		print("Degrees: [%d,%d,%d]\n" % (acs,afs,ats))
	return [acs,afs,ats]

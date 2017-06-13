#!/usr/bin/python3

from time import sleep
import math



def legIk(x = 0, y = 0, z = 0, values = None):
        if values != None:
                x = values[0]
                y = values[1]
                z = values[2]
	#legIk(130.19, 0, 74.90)
	#servo omhoog is 512+, servo naar rechts is -
	#feetpos
	#posX = 130.12
	#posY = 0

	pifactor = 180 / math.pi
	radfactor = math.pi / 180
	
	e = z
	f = 37
	a = 67.19
	c = 137.51
        
	l = x
	coxaalphamax = 54
	coxaalphamaxhalf = (0.5 * coxaalphamax )* radfactor

	ac = math.atan(y/x) * pifactor

	#print (ac)
	
	smallestl = math.cos(coxaalphamaxhalf) * l

	totalstep = 2 * math.sqrt(math.pow(l,2) - math.pow(smallestl,2))

	#if ac > (0.5 * coxaalphamax):
		#ac = abs(ac) - (0.5 * coxaalphamax)
	#else:
		#ac = (0.5 * coxaalphamax) - abs(ac)

	#print (ac)
	
	laccent = smallestl / (math.cos(ac * radfactor))

	#print (laccent)
	
	d = laccent - f

	b = math.sqrt(math.pow(d,2) + math.pow(e,2))

	alpha = (math.acos((math.pow(a,2) - math.pow(c,2) - math.pow(b,2))/(-2 * c * b))) * pifactor

	gamma = (math.acos((math.pow(c,2) - math.pow(b,2) - math.pow(a,2))/(-2 * b * a))) * pifactor

	beta = (math.acos((math.pow(b,2) - math.pow(a,2) - math.pow(c,2))/(-2 * a * c))) * pifactor

	delta = math.atan(d/e) * pifactor

	epsilon = math.atan(e/d) * pifactor

	alphaepsilon = alpha + epsilon

	
	af = (gamma - epsilon) + 14

	at = 121.1 - beta
        
	sfactor = 1024.00/300
	
	acs = (1024 - ((ac + 150) * sfactor))
	afs = (af + 150) * sfactor
	ats = (150 - at) * sfactor
	

	
	return [acs,afs,ats]

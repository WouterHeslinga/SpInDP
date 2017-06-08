#!/usr/bin/python3

from time import sleep
import math

def legIk(x, y, z):
        #legIk(130.19, 0, 74.90)
        #servo omhoog is 512+, servo naar rechts is -
        #feetpos
        #posX = 130.12
        #posY = 0
        #posZ = 74.90
        lc = 37
        lf = 67.19
        lt = 137.51
        #dist = distance from coxa to foot in x,y
        dist = 130.12

        b = math.sqrt(math.pow(z,2) + math.pow(dist,2))

        #angles
        # c = coxa
        # f = femur
        # t = tibia
        ac = math.degrees(math.atan(y/x))
        
        t1 = math.atan(dist/z)
        t2 = math.acos((math.pow(lf,2) +  math.pow(b,2) - math.pow(lt,2))/(2 * lf * lt))

        ti = math.acos((math.pow(lf,2) + math.pow(lt,2) - math.pow(b,2))/(2 * lf * lt))              
        

        

        af = math.degrees(t1) + math.degrees(t2) - 76

        at = 121 - math.degrees(ti)
        

        # s = servo
        sfactor = 1023.00/300

        acs = (-ac + 150) * sfactor
        afs = (af + 150) * sfactor
        ats = (-at + 150) * sfactor

        #print("\n[acs: " + str(acs) + ", afs: " + str(afs) + ", ats: " + str(ats) + "]")

        return [acs,afs,ats]

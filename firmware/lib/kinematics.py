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
        #posZ = 74.90
        lc = 37
        lf = 67.19
        lt = 137.51
        lb = 130.12
        #lb = math.sqrt(math.pow(x,2) + math.pow(y,2) + math.pow(z,2))

        #angles
        # c = coxa
        # f = femur
        # t = tibia
        ac = math.degrees(math.atan(y/x))
        
        a1 = math.atan((lb-lc)/-z)
        hf = math.sqrt(math.pow((lb - lc),2) + math.pow(z, 2))

        a2 = math.acos((math.pow(lt, 2) - math.pow(lf, 2) - math.pow(hf, 2))/(-2 * lf * hf))
        af = 90 - (math.degrees(a1) + math.degrees(a2)) + 14

        b1 = math.acos((math.pow(hf, 2) - math.pow(lt, 2) - math.pow(lf, 2))/(-2 * lt * lf))
        #at + additional frame angle of 58.91
        at = (180 - math.degrees(b1) - 58.91)
        

        # s = servo
        sfactor = 1023.00/300

        acs = (ac + 150) * sfactor
        afs = (af + 150) * sfactor
        ats = (-at + 150) * sfactor

        #print("\n[acs: " + str(acs) + ", afs: " + str(afs) + ", ats: " + str(ats) + "]")

        return [acs,afs,ats]


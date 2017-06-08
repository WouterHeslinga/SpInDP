#!/usr/bin/python3

import threading
from time import sleep
from random import randint
import Tkinter as tk
import kinematics as ik


class debugThread (threading.Thread):
        def __init__(self, threadID, name, legs, servos):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.name = name
                self.legs = legs
                self.servos = servos
	def run(self):
                self.s_print ("Starting... ")
                self.setupWindow()
        def stop(self):
                self.root.destroy()

	def setupWindow(self):
                #Scale values
                hipMin = -500
                hipMax = 500
                kneeMin = -500
                kneeMax = 500
                footMin = -500
                footMax = 500
                sliderInterval = 100

                rowCounter = 0
                
                #create debug window
                root = tk.Tk()
                root.minsize(width=1200, height=500)
                root.maxsize(width=1200, height=1000)

                rowCounter += 1
                

                tk.Label(root, text="x", bg="red", fg="white").grid(row=rowCounter, column=1)
                tk.Label(root, text="y", bg="red", fg="white").grid(row=rowCounter, column=2)
                tk.Label(root, text="z", bg="red", fg="white").grid(row=rowCounter, column=3)

        
                rowCounter += 1

                tk.Label(root, text="all", bg="red", fg="white").grid(row=rowCounter, column=0)
                
                self.hipAll = tk.Scale(root, from_=hipMin, to=hipMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.hipAll.set(0)  
                self.hipAll.grid(row=rowCounter, column=1)       
                self.kneeAll = tk.Scale(root, from_=kneeMin, to=kneeMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.kneeAll.set(0)   
                self.kneeAll.grid(row=rowCounter, column=2)        
                self.footAll = tk.Scale(root, from_=footMin, to=footMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.footAll.set(0)
                self.footAll.grid(row=rowCounter, column=3)

                tk.Button(root, text="Apply All", command=lambda: self.set_all()).grid(row=rowCounter,column=4)
                tk.Button(root, text="Apply Even", command=lambda: self.set_even()).grid(row=rowCounter, column=5)
                tk.Button(root, text="Apply Uneven", command=lambda: self.set_uneven()).grid(row=rowCounter, column=6)

                rowCounter += 1

                tk.Label(root, text="leg 1", bg="red", fg="white").grid(row=rowCounter, column=0)

                self.hip1 = tk.Scale(root, from_=hipMin, to=hipMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.hip1.set(0)  
                self.hip1.grid(row=rowCounter, column=1)       
                self.knee1 = tk.Scale(root, from_=kneeMin, to=kneeMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.knee1.set(0)   
                self.knee1.grid(row=rowCounter, column=2)        
                self.foot1 = tk.Scale(root, from_=footMin, to=footMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.foot1.set(0)
                self.foot1.grid(row=rowCounter, column=3)

                tk.Button(root, text="Apply", command=lambda: self.set_leg(1)).grid(row=rowCounter,column=4)

                rowCounter += 1

                tk.Label(root, text="leg 2", bg="red", fg="white").grid(row=rowCounter, column=0)

                self.hip2 = tk.Scale(root, from_=hipMin, to=hipMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.hip2.set(0)  
                self.hip2.grid(row=rowCounter, column=1)       
                self.knee2 = tk.Scale(root, from_=kneeMin, to=kneeMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.knee2.set(0)   
                self.knee2.grid(row=rowCounter, column=2)       
                self.foot2 = tk.Scale(root, from_=footMin, to=footMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.foot2.set(0)
                self.foot2.grid(row=rowCounter, column=3)

                tk.Button(root, text="Apply", command=lambda: self.set_leg(2)).grid(row=rowCounter,column=4)
                
                rowCounter += 1

                tk.Label(root, text="leg 3", bg="red", fg="white").grid(row=rowCounter, column=0)

                self.hip3 = tk.Scale(root, from_=hipMin, to=hipMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.hip3.set(0)  
                self.hip3.grid(row=rowCounter, column=1)       
                self.knee3 = tk.Scale(root, from_=kneeMin, to=kneeMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.knee3.set(0)   
                self.knee3.grid(row=rowCounter, column=2)       
                self.foot3 = tk.Scale(root, from_=footMin, to=footMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.foot3.set(0)
                self.foot3.grid(row=rowCounter, column=3)

                tk.Button(root, text="Apply", command=lambda: self.set_leg(3)).grid(row=rowCounter,column=4)

                rowCounter += 1

                tk.Label(root, text="leg 4", bg="red", fg="white").grid(row=rowCounter, column=0)

                self.hip4 = tk.Scale(root, from_=hipMin, to=hipMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.hip4.set(0)  
                self.hip4.grid(row=rowCounter, column=1)       
                self.knee4 = tk.Scale(root, from_=kneeMin, to=kneeMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.knee4.set(0)   
                self.knee4.grid(row=rowCounter, column=2)       
                self.foot4 = tk.Scale(root, from_=footMin, to=footMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.foot4.set(0)
                self.foot4.grid(row=rowCounter, column=3)

                tk.Button(root, text="Apply", command=lambda: self.set_leg(4)).grid(row=rowCounter,column=4)

                rowCounter += 1

                tk.Label(root, text="leg 5", bg="red", fg="white").grid(row=rowCounter, column=0)

                self.hip5 = tk.Scale(root, from_=hipMin, to=hipMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.hip5.set(0)  
                self.hip5.grid(row=rowCounter, column=1)       
                self.knee5 = tk.Scale(root, from_=kneeMin, to=kneeMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.knee5.set(0)   
                self.knee5.grid(row=rowCounter, column=2)       
                self.foot5 = tk.Scale(root, from_=footMin, to=footMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.foot5.set(0)
                self.foot5.grid(row=rowCounter, column=3)

                tk.Button(root, text="Apply", command=lambda: self.set_leg(5)).grid(row=rowCounter,column=4)

                rowCounter += 1

                tk.Label(root, text="leg 6", bg="red", fg="white").grid(row=rowCounter, column=0)

                self.hip6 = tk.Scale(root, from_=hipMin, to=hipMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.hip6.set(0)  
                self.hip6.grid(row=rowCounter, column=1)       
                self.knee6 = tk.Scale(root, from_=kneeMin, to=kneeMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.knee6.set(0)   
                self.knee6.grid(row=rowCounter, column=2)       
                self.foot6 = tk.Scale(root, from_=footMin, to=footMax, length=300, tickinterval=sliderInterval, orient="horizontal")
                self.foot6.set(0)
                self.foot6.grid(row=rowCounter, column=3)

                tk.Button(root, text="Apply", command=lambda: self.set_leg(6)).grid(row=rowCounter,column=4)

                rowCounter += 1

                tk.Button(root, text="Read", command=lambda: self.get_all()).grid(row=rowCounter,column=4)

                # apply current servo values to sliders
                self.get_all()

                self.root = root
                self.root.mainloop()


            
        def show_values(self,w1,w2,w3):
                #self.s_print(str(w1.get()) + " " + str(w2.get()) + " " + str(w3.get()))
                self.s_print("emtpy")

        def get_all(self):
                for leg in self.legs:
                        try:
                                values = self.get_sliders_by_id(leg.id)
                                values[0].set(leg.hip.getAngle())
                                values[1].set(leg.knee.getAngle())
                                values[2].set(leg.foot.getAngle())
                        except Exception as ex:
                                self.s_print(str(ex))
                        
        

        def set_all(self):
                for leg in self.legs:
                        values = ik.legIk(int(self.hipAll.get()),int(self.kneeAll.get()),int(self.footAll.get()))
                        leg.move(values)
     
                self.get_all()


        def set_leg(self,id):
                values = self.get_sliders_by_id(id)
                values = ik.legIk(int(values[0]),int(values[1]),int(values[2]))
                self.legs[id - 1].move(values)

        def set_even(self):
                even = [2,4,6]
                for leg in self.legs:
                        if leg.id in even:
                                values = ik.legIk(int(self.hipAll.get()),int(self.kneeAll.get()),int(self.footAll.get()))
                                self.legs[id - 1].move(values)          
                self.get_all()

        def set_uneven(self):
                uneven = [1,3,5]
                for leg in self.legs:
                        if leg.id in uneven:
                                values = ik.legIk(int(self.hipAll.get()),int(self.kneeAll.get()),int(self.footAll.get()))
                                self.legs[id - 1].move(values) 
  
                self.get_all()

        def get_sliders_by_id(self,id):
                if id == 1:
                        return [self.hip1, self.knee1, self.foot1]
                elif id == 2:
                        return [self.hip2, self.knee2, self.foot2]
                elif id == 3:
                        return [self.hip3, self.knee3, self.foot3]
                elif id == 4:
                        return [self.hip4, self.knee4, self.foot4]
                elif id == 5:
                        return [self.hip5, self.knee5, self.foot5]
                elif id == 6:
                        return [self.hip6, self.knee6, self.foot6]
                #else:
                #        return [512,512,512]
                
            
                        
        def s_print(self, message):
                print("[" + self.name + "] " + str(message))

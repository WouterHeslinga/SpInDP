from time import sleep
import lib.servo as servo
import lib.leg2 as leg
import lib.animations as animation
import threading

class MotionController:
    def __init__(self, queue, main_queue):
        self.servos = None
        self.legs = None
        self.initialize_legs()
        self.queue = queue
        self.state = "idle"
        self.main_queue = main_queue
        self.should_run = True
        self.event = threading.Event()

    def run(self):
        worker = threading.Thread(target=self.queue_worker)
        worker.start()
        while True:
            self.event.wait(2)
            servo_inf = self.get_servo_info()
            self.main_queue.put({'servo_info': servo_inf})
    
    def queue_worker(self):
        while self.should_run:
            if not self.queue.empty():
                command = self.queue.get()
                print("Motion received command: %s" % ', '.join(command))
            self.event.wait(.5)
    
    def get_servo_info(self):
        try:
            info = []
            info.append(str(80)) #battery
            info.append(str(0)) #angle
            for servo in self.servos:
                info.append(str(servo.getTemperature()))
                info.append(str(servo.getAngle()))
            
            return ';'.join(info)
        except:
            return None

    def initialize_legs(self):
        self.servos = servo.readServoMappings()
        self.legs = self.map_legs(self.servos)

    def map_legs(self, servos):
        legs = []
        knees = {}
        hips = {}
        feet = {}
        for servo in servos:
            if servo.joint == "knee":
                knees[servo.leg] = servo
            elif servo.joint == "hip":
                hips[servo.leg] = servo
            elif servo.joint == "foot":
                feet[servo.leg] = servo

            if servo.leg in knees and servo.leg in hips and servo.leg in feet:
                legs.append(leg.Leg(servo.leg, hips[servo.leg], knees[servo.leg], feet[servo.leg]))
        return legs
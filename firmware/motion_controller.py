from time import sleep
import lib.servo as servo
import lib.leg2 as leg
import lib.animations as animations
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

        self.angle = 0
        self.animation = None
        self.timeout = 0.5
        self.totalKeyframes = -1
        self.keyframeEven = 0
        self.keyframeUneven = 0

    def run(self):
        worker = threading.Thread(target=self.queue_worker)
        worker.start()
        while True:
            servo_info_interval = 1.0
            servo_info_timer = 0.0

            if self.state != "idle" or self.animation != None:
                animation = self.animation
                # set legs to start position
                for leg in self.legs:
                    animation(0, leg, angle=self.angle)
                sleep(self.timeout)
                servo_info_timer += self.timeout

                self.setup_keyframes()

                totalKeyframes = self.totalKeyframes
                legs = self.legs

                # play animation
                state = self.state
                while state == self.state:
                    for leg in legs:
                        if leg.isEven:
                            animation(self.keyframeEven, leg, angle=self.angle)
                        else:
                            animation(self.keyframeUneven, leg, angle=self.angle)

                    self.keyframeEven += 1
                    self.keyframeUneven += 1

                    if self.keyframeEven > totalKeyframes:
                        self.keyframeEven = 1
                    if self.keyframeUneven > totalKeyframes:
                        self.keyframeUneven = 1
                    sleep(self.timeout)
                    servo_info_timer += self.timeout

                    if servo_info_timer > servo_info_interval:
                        servo_info = self.get_servo_info()
                        self.main_queue.put({'servo_info': servo_info}) 
                        print("servoINF")  
                        servo_info_timer = 0

            
            self.event.wait(0.05)
            servo_info_timer += 0.05

            if servo_info_timer > servo_info_interval:
                servo_info = self.get_servo_info()
                self.main_queue.put({'servo_info': servo_info})
                print("servoINF") 
                servo_info_timer = 0
    
    def queue_worker(self):
        while self.should_run:
            if not self.queue.empty():
                command = self.queue.get()
                print(command)
                if 'motion_state' in command:
                    print("yes")
                    new_state = command["motion_state"]
                    print(new_state)
                    if self.state == new_state:
                        try:
                            angleValue = int(new_state)
                            self.angle = angleValue
                        except:
                            pass
                        continue

                    if new_state == "idle":
                        self.angle = 0
                        self.animation = None
                        self.timeout = 0.5
                        self.totalKeyframes = -1
                        self.state = "idle"                 
                    else:
                        self.angle = int(new_state)
                        self.animation = animations.walk
                        self.timeout = 0.2
                        self.totalKeyframes = 4
                        self.state = "walk"

            self.event.wait(.1)   
    
    def setup_keyframes(self, synced=False):
        if synced == True:
            keyframeEven = 1
            keyframeUneven = 1
            return

        self.keyframeEven = self.totalKeyframes / self.totalKeyframes
        if self.totalKeyframes == 1:
            self.keyframeUneven = 1
        else:
            self.keyframeUneven = self.totalKeyframes / 2 + 1

    def get_servo_info(self):
        try:
            info = ""
            info = info + str(80)
            info = info + ";" + str(0)
            for servo in self.servos:
                info = info + ';' + str(servo.getTemperature()) + ',' + str(servo.getAngle());
                sleep(0.001)
            
            return info
        except:
            return None

    def initialize_legs(self):
        self.servos = servo.readServoMappings()
        legs = []
        knees = {}
        hips = {}
        feet = {}

        for s in self.servos:
            if s.joint == "knee":
                knees[s.leg] = s
            elif s.joint == "hip":
                hips[s.leg] = s
            elif s.joint == "foot":
                feet[s.leg] = s

            if s.leg in knees and s.leg in hips and s.leg in feet:
                legs.append(leg.Leg(s.leg, hips[s.leg], knees[s.leg], feet[s.leg]))
        self.legs = legs
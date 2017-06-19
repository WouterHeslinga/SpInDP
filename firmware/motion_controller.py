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

        self.angle = 0

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
                if "motion_state" in command:
                    info = command["motion_state"]

                    print("Motion received command: %s" % ', '.join(info))
                    
                    if info[0] == "idle":
                        continue
                    
                    else:
                        self.angle = int(info[1])
                        """if info[0] == "0":
                            self.angle = int(info[1])
                            continue
                        if info[0] == "90":
                            self.angle = int(info[1])
                            continue
                        if info[0] == "180":
                            self.angle = int(info[1])
                            continue
                        if info[0] == "270":
                            self.angle = int(info[1])
                            continue"""
                        self.play_animation(animation.walk, 4, 0.17)

            self.event.wait(.5)

    def play_animation(self, animation, totalKeyframes, timeout = 0.2):
        legs = self.legs

        # set legs to default position
        for leg in legs:
            leg.changePos(130,0,100, add=False)
            
        sleep(1)

        # set legs to start position
        for leg in legs:
            animation(0, leg, angle=self.angle)
            
        sleep(timeout)

        # play animation
        keyframeEven = totalKeyframes / totalKeyframes
        if totalKeyframes == 1:
            keyframeUneven = 1
        else:
            keyframeUneven = totalKeyframes / 2 + 1
            
        while self.queue.empty():
            for leg in legs:
                if leg.isEven:
                    animation(keyframeEven, leg, angle=self.angle)
                else:
                    animation(keyframeUneven, leg, angle=self.angle)

            keyframeEven += 1
            keyframeUneven += 1

            if keyframeEven > totalKeyframes:
                keyframeEven = 1
            if keyframeUneven > totalKeyframes:
                keyframeUneven = 1
            sleep(timeout)
    
    def get_servo_info(self):
        try:
            info = ""
            info = info + str(80)
            info = info + ";" + str(0)
            for servo in self.servos:
                info = info + ';' + str(servo.getTemperature()) + ',' + str(servo.getAngle());
            
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
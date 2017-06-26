from time import sleep
import lib.servo as servo
import lib.leg as leg
import lib.animations as animations
import threading

class MotionController:
    def __init__(self, queue, main_queue):
        sleep(0.2)
        self.servos = None
        self.legs = None
        self.initialize_legs()
        self.queue = queue
        self.state = "idle"

        self.main_queue = main_queue
        self.should_run = True
        self.event = threading.Event()

        self.angle = 0
        self.rotateDirection = "None"
        self.spanWidth = 130
        self.bodyHeight = 100
        self.rollx = 0
        self.pitchy = 0
        self.yawz = 0
        self.statusValues = [self.angle, self.rotateDirection, self.spanWidth, self.bodyHeight, self.rollx, self.pitchy, self.yawz]

        self.animation = animations.idle
        self.timeout = 0.5
        self.totalKeyframes = -1
        self.keyframeEven = 0
        self.keyframeUneven = 0

    def run(self):
        worker = threading.Thread(target=self.queue_worker)
        worker.start()
        while True:
            legs = self.legs
            state = self.state

            servo_info_interval = 1.0
            servo_info_timer = 0.0

            # if state is anything but idle
            if self.state != "idle" and self.animation is not None:
                totalKeyframes = self.totalKeyframes

                # set legs to start position
                for leg in self.legs:
                    self.play_animation(0, leg)

                # play animation
                if totalKeyframes <= 0:
                    while state == self.state:
                        sleep(self.timeout)
                        servo_info_timer += self.timeout
                        if servo_info_timer > servo_info_interval:
                            servo_info = self.get_servo_info()
                            self.main_queue.put({'servo_info': servo_info}) 
                            servo_info_timer = 0
                else:
                    while state == self.state:
                        """self.play_animation(self.keyframeEven, legs[0])
                        self.play_animation(self.keyframeUneven, legs[3])
                        sleep(self.timeout/3)
                        self.play_animation(self.keyframeEven, legs[1])
                        self.play_animation(self.keyframeUneven, legs[4])
                        sleep(self.timeout/3)
                        self.play_animation(self.keyframeEven, legs[2])
                        self.play_animation(self.keyframeUneven, legs[5])"""
                                
                        for leg in legs:
                            if leg.isEven:
                                self.play_animation(self.keyframeEven, leg)
                            else:
                                self.play_animation(self.keyframeUneven, leg)

                        self.keyframeEven += 1
                        self.keyframeUneven += 1

                        if self.keyframeEven > totalKeyframes: self.keyframeEven = 1
                        if self.keyframeUneven > totalKeyframes: self.keyframeUneven = 1

                        sleep(self.timeout)
                        servo_info_timer += self.timeout

                        if servo_info_timer > servo_info_interval:
                            servo_info = self.get_servo_info()
                            self.main_queue.put({'servo_info': servo_info}) 
                            servo_info_timer = 0

            # if state is idle
            elif self.state == "idle" and self.animation is not None:
                while state == self.state:
                    for leg in legs:
                        self.play_animation(0, leg)

                    sleep(self.timeout)
                    servo_info_timer += self.timeout

                    if servo_info_timer > servo_info_interval:
                            servo_info = self.get_servo_info()
                            self.main_queue.put({'servo_info': servo_info}) 
                            servo_info_timer = 0

            
            sleep(0.1)
            servo_info_timer += 0.1

            if servo_info_timer > servo_info_interval:
                servo_info = self.get_servo_info()
                self.main_queue.put({'servo_info': servo_info})
                servo_info_timer = 0
    
    def queue_worker(self):
        while self.should_run:
            if not self.queue.empty():
                # process command
                command = self.queue.get()

                # motion commands are for changing specific variables (height, angle, yaw, pitch etc.)
                # example: 'height:100'
                if 'motion_command' in command:
                    new_command = command['motion_command']
                    if new_command is None:
                        continue

                    # try to get a valid value
                    try:
                        seperator = new_command.index(":")
                        new_value = int(new_command[seperator + 1:])
                        new_command = new_command[:seperator]

                        if new_command == "height":
                            self.bodyHeight = new_value

                        elif new_command == "angle":
                            self.angle = new_value

                    except:
                        print("Invalid motion_command")


                # motion states are for changing the movement animation
                # example: '0', '90', 'idle'
                elif 'motion_state' in command:
                    new_state = command["motion_state"]
                    if new_state is None or new_state == self.state:
                        continue

                    # try to get an angle value and expect the walk state, else expect a different state
                    try:
                        angleValue = int(new_state)
                        # update current walk state with new angle
                        if self.state == "walk":
                            #if angleValue - self.angle > 5 and angleValue - self.angle < -5:
                            #    continue
                            self.angle = angleValue

                        # activate walk state   
                        else:
                            self.angle = int(new_state)
                            self.rotateDirection = "none"
                            self.animation = animations.walk
                            self.timeout = 0.1
                            self.totalKeyframes = 4
                            self.setup_keyframes()
                            self.state = str(new_state)
                    except:
                        if new_state == "idle":
                            print("switching to idle")
                            self.angle = 0
                            self.animation = animations.idle
                            self.timeout = 0.5
                            self.totalKeyframes = -1
                            self.setup_keyframes()
                            self.state = str(new_state)

                        elif new_state == "rotate_left":
                            print("switching to left")
                            self.angle = 0
                            self.rotateDirection = "left"
                            self.animation = animations.walk
                            self.timeout = 0.2
                            self.totalKeyframes = 4
                            self.setup_keyframes()
                            self.state = str(new_state)

                        elif new_state == "rotate_right":
                            print("switching to right")
                            self.angle = 0
                            self.rotateDirection = "right"
                            self.animation = animations.walk
                            self.timeout = 0.2
                            self.totalKeyframes = 4
                            self.setup_keyframes()
                            self.state = str(new_state)

                        elif new_state == "clap":
                            self.angle = 0
                            self.animation = animations.balloon
                            self.timeout = .5
                            self.totalKeyframes = 3
                            self.state = str(new_state)

                        elif new_state == "twerk":
                            self.angle = 0
                            self.animation = animations.twerk
                            self.timeout = .3
                            self.totalKeyframes = 2
                            self.state = str(new_state)
                            
                        elif new_state == "greet":
                            self.angle = 0
                            self.animation = animations.greet
                            self.timeout = .3
                            self.totalKeyframes = 2
                            self.state = str(new_state)

                        elif new_state == "dab":
                            self.angle = 0
                            self.animation = animations.dab
                            self.timeout = .3
                            self.totalKeyframes = 2
                            self.state = str(new_state)


            self.event.wait(.1)   
    
    def setup_keyframes(self, synced=False):
        if self.totalKeyframes < 1:
            self.keyframeEven = 0
            self.keyframeUneven = 0
            return
        
        if synced == True:
            keyframeEven = 1
            keyframeUneven = 1
            return

        self.keyframeEven = self.totalKeyframes / self.totalKeyframes
        if self.totalKeyframes == 1:
            self.keyframeUneven = 1
        else:
            self.keyframeUneven = self.totalKeyframes / 2 + 1

    def play_animation(self, keyframe, leg):
        self.statusValues = [self.angle, self.rotateDirection, self.spanWidth, self.bodyHeight, self.rollx, self.pitchy, self.yawz]
        self.animation(keyframe, leg, self.statusValues)


    def get_servo_info(self):
        try:
            info = ""
            info = info + str(80)
            info = info + ";" + str(0)
            for servo in self.servos:
                info = info + ';' + str(servo.getTemperature()) + ',' + str(servo.getAngle());
                sleep(0.002)
            
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

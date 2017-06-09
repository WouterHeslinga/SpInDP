from time import sleep


class MotionController:
    def __init__(self, queue):
        self.test = "Test"
        self.queue = queue

    def update(self):
        while True:
            sleep(1)


class Leg:
    def __init__(self):
        self.test = "Test"


class Servo:
    def __init__(self):
        self.test = "Test"

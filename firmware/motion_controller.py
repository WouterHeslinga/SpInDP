from time import sleep
import threading

class MotionController:
    def __init__(self, queue):
        self.test = "Test"
        self.queue = queue

    def run(self):
        worker = threading.Thread(target=self.queue_worker)
        while True:
            sleep(1)
    
    def queue_worker(self):
        while self.should_run:
            if not self.queue.empty():
                command = self.queue.get()
                print("Motion recieved command: %s" % commanf.join(', '))
                
            self.event.wait(.5)

class Leg:
    def __init__(self):
        self.test = "Test"


class Servo:
    def __init__(self):
        self.test = "Test"

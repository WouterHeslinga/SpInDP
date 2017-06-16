from time import sleep
import threading

class MotionController:
    def __init__(self, queue, main_queue):
        self.test = "Test"
        self.queue = queue
        self.main_queue = main_queue
        self.should_run = True
        self.event = threading.Event()

    def run(self):
        worker = threading.Thread(target=self.queue_worker)
        worker.start()
        while True:
            self.event.wait(1)
            self.main_queue.put({'temps': range(1,19)})
    
    def queue_worker(self):
        while self.should_run:
            if not self.queue.empty():
                command = self.queue.get()
                print("Motion recieved command: %s" % ', '.join(command))
                
            self.event.wait(.5)

class Leg:
    def __init__(self):
        self.test = "Test"


class Servo:
    def __init__(self):
        self.test = "Test"

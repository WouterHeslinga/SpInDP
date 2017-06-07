from flask import Flask, jsonify
import threading

class Web:
    """Web interface"""
    def __init__(self, queue):
        self.event = threading.Event()
        self.queue = queue
        self.status = None
        self.web = Flask(__name__)
        self.web.add_url_rule('/', 'index', self.index)
        self.web.add_url_rule('/status', 'get_status', self.get_status)
        self.should_run = True

    def index(self):
        return 'Hello World'
    
    def get_status(self):
        if self.status is None:
            return '{}'
        else:
            return jsonify(self.status)

    def queue_worker(self):
        while self.should_run:
            if not self.queue.empty():
                status = self.queue.get()
                self.status = status
                
            self.event.wait(.5)

    def run(self):
        queue_thread = threading.Thread(target=self.queue_worker)
        queue_thread.start()

        self.web.run()
    
    def stop(self):
        self.should_run = False
        self.event.set()

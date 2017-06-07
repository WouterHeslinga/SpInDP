import multiprocessing
from time import sleep
from web import Web
from vision import Vision

def vision_worker(q):
    """Worker for the vision"""
    print("Starting Vision Worker")
    vision = Vision(True, q)
    while True:
        vision.update()
    return

def web_Worker(q):
    """Worker for the web interface"""
    print("Starting web Worker")
    web = Web(q)
    web.run()
    return

if __name__ == '__main__':
    workers = []
    queue_vision_web = multiprocessing.Queue()

    # Create the workers
    workers.append(multiprocessing.Process(target=vision_worker, args=(queue_vision_web,)))
    workers.append(multiprocessing.Process(target=web_Worker, args=(queue_vision_web,)))
    
    # Start the workers
    for worker in workers:
        worker.start()

    # Join the workers
    for worker in workers:
        worker.join()
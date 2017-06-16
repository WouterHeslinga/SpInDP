import multiprocessing
from time import sleep
from web import Web
from vision import Vision
from motion_controller import MotionController
from bluetooth_server import BluetoothServer
from threading import Event


def vision_worker(queue):
    """Worker for the vision"""
    print("Starting vision worker")
    vision = Vision(True, queue)
    while True:
        vision.update()
    return


def web_worker(queue):
    """Worker for the web interface"""
    print("Starting web worker")
    web = Web(queue)
    web.run()
    return


def motion_controller_worker(queue, queue_main):
    """Worker for the leg controller"""
    print("Starting leg controller worker")
    motion = MotionController(queue, queue_main)
    motion.run()

def bluetooth_server_worker(queue, queue_main):
    """Worker for the bluetooth server"""
    print("Starting bluetooth worker")
    bluetooth = BluetoothServer(queue, queue_main, 1)
    bluetooth.run()
    return

if __name__ == '__main__':
    should_run = True
    event = Event()
    workers = []
    queue_main = multiprocessing.Queue()
    queue_motion = multiprocessing.Queue()
    queue_bluetooth = multiprocessing.Queue()

    # Create the workers
    # workers.append(multiprocessing.Process(target=vision_worker, args=(queue_vision_web,)))
    # workers.append(multiprocessing.Process(target=web_worker, args=(queue_vision_web,)))
    workers.append(multiprocessing.Process(target=motion_controller_worker, args=(queue_motion, queue_main)))
    workers.append(multiprocessing.Process(target=bluetooth_server_worker, args=(queue_bluetooth, queue_main)))

    # Start the workers
    for worker in workers:
        worker.start()

    while should_run:   
        event.wait(.5)
        if not queue_main.empty():
            commands = queue_main.get()
            if 'temps' in commands:
                print(commands['temps'])

    # Join the workers
    for worker in workers:
        worker.join()

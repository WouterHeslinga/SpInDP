import multiprocessing
from time import sleep
from web import Web
from vision import Vision
from motion_controller import MotionController
from bluetooth_server import BluetoothServer


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


def motion_controller_worker():
    """Worker for the leg controller"""
    print("Starting leg controller worker")
    motion = MotionController()
    motion.update()


def bluetooth_server_worker():
    """Worker for the bluetooth server"""
    print("Starting bluetooth debugApp worker")
    bluetoothapp = BluetoothServer("debugApp", [1-6], [1-18])
    print("Starting bluetooth controller worker")
    bluetoothcontroller = BluetoothServer("controller", [1-6], [1-18])

if __name__ == '__main__':
    workers = []
    queue_vision_web = multiprocessing.Queue()

    # Create the workers
    workers.append(multiprocessing.Process(target=vision_worker, args=(queue_vision_web,)))
    workers.append(multiprocessing.Process(target=web_worker, args=(queue_vision_web,)))
    workers.append(multiprocessing.Process(target=motion_controller_worker))
    workers.append(multiprocessing.Process(target=bluetooth_server_worker))

    # Start the workers
    for worker in workers:
        worker.start()

    # Join the workers
    for worker in workers:
        worker.join()

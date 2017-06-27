import multiprocessing
from time import sleep
from web import Web
from vision import Vision
from motion_controller import MotionController
from bluetooth_server import BluetoothServer
from threading import Event
import sys


def vision_worker(queue, main_queue):
    """Worker for the vision"""
    print("Starting vision worker")
    vision = Vision(queue, main_queue)
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

def bluetooth_server_worker(server):
    """Worker for the bluetooth server"""
    print("Starting bluetooth worker")
    server.run()
    return

if __name__ == '__main__':
    should_run = True
    event = Event()
    workers = []
    queue_main = multiprocessing.Queue()
    queue_motion = multiprocessing.Queue()
    queue_bluetooth = multiprocessing.Queue()
    queue_vision = multiprocessing.Queue()
    bluetooth = BluetoothServer(queue_bluetooth, queue_main, 1)

    # Create the workers
    # workers.append(multiprocessing.Process(target=vision_worker, args=(queue_vision, queue_main)))
    # workers.append(multiprocessing.Process(target=web_worker, args=(queue_vision_web,)))
    workers.append(multiprocessing.Process(target=motion_controller_worker, args=(queue_motion, queue_main)))
    workers.append(multiprocessing.Process(target=bluetooth_server_worker, args=(bluetooth,)))

    # Start the workers
    for worker in workers:
        worker.start()

    try:
        while should_run:   
            queue_main.put({'motion_state': raw_input("direction: ")})
            #queue_main.put({'motion_command': raw_input("command: ")})
            sleep(0.04)
            if not queue_main.empty():
                commands = queue_main.get()
                if 'servo_info' in commands:
                    queue_bluetooth.put({'servo_info': commands['servo_info']})

                elif 'motion_command' in commands:
                    queue_motion.put({'motion_command': commands['motion_command']})
                elif 'motion_state' in commands:
                    queue_motion.put({'motion_state': commands['motion_state']})
                elif 'objectcoords' in commands:
                    queue_motion.put({'motion_state': commands['objectcoords']})

                elif 'egg' in commands:
                    queue_vision.put({'egg': commands['egg']})

    except KeyboardInterrupt:
        print('closing bluetooth')
        bluetooth.close()
        sys.exit()

    # Join the workers
    for worker in workers:
        worker.join()

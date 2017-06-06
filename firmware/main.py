import multiprocessing
from time import sleep
from web import Web

def vision_worker(q):
    """Worker for the vision"""
    print("Starting Vision Worker")
    for i in range(10):
        print("Polling vision")
        sleep(1)
    print('Stopping vision worker')
    return

def web_Worker(q):
    """Worker for the web interface"""
    print("Starting web Worker")
    web = Web()
    web.run()
    return

if __name__ == '__main__':
    workers = []
    queue_vision_web = multiprocessing.Queue()

    workers.append(multiprocessing.Process(target=vision_worker, args=(queue_vision_web,)))
    workers.append(multiprocessing.Process(target=web_Worker, args=(queue_vision_web,)))

    # Start the workers
    for worker in workers:
        worker.start()

    # Join the workers
    for worker in workers:
        worker.join()
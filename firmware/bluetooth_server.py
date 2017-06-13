import socket
import json
import threading

from time import sleep
from random import randint

class BluetoothServer:
    def __init__(self, queue, port=1):
        self.workers = []
        self.port = port
        self.queue = queue
        self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    def run(self):
        print("Starting server")
        self.socket.bind(("00:1A:7D:DA:71:12", self.port))
        self.socket.listen(5)

        while True:
            client, address = self.socket.accept()
            client.settimeout(60)
            worker = threading.Thread(target=self.worker, args=(client, address))
            self.workers.append(worker)
            worker.start()

    def worker(self, client, address):
        size = 1024
        print("Client %s connected" % address[0])

        data = ""
        while True:
            try:
                data = data + client.recv(size)
                print(data)
                while True:
                    end = data.find('\n')
                    if end == -1:
                        break
                    
                    command = data[:end]
                    data = data[end+1:]
                    split = data.split(":")
                    self.queue.put(split)
                    print("Server recieved: %s" % ", ".join(split))

            except Exception as ex:
                client.close()
                print("Client %s disconnected" % address[0])
                print(ex)
                return False
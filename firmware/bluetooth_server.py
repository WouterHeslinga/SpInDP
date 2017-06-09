import socket
import json
import threading

from time import sleep
from random import randint

class BluetoothServer:
    def __init__(self, queue, port=1):
        self.workers = []
        self.port = port
        self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    def run(self):
        print("Starting server")
        self.socket.bind(("00:1A:7D:DA:71:12", self.port))
        self.socket.listen(5)

        while True:
            client, address = self.socket.accept()
            client.settimeout(60)
            worker = threading.Thread(target=worker, args=(client, address))
            self.workers.append(worker)
            worker.start()

    def worker(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    print(data)
                else:
                    raise "Client disconnected"
            except:
                client.close()
                return false
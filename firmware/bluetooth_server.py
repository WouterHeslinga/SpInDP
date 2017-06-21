import socket
import json
import threading
import traceback

from time import sleep
from random import randint

class BluetoothServer:
    def __init__(self, queue, main_queue, port=1):
        self.data = {}
        self.workers = []
        self.port = port
        self.queue = queue
        self.main_queue = main_queue
        self.event = threading.Event()
        self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.servo_info = None

    def queue_reader(self):
        while True:
            self.event.wait(.2)
            if not self.queue.empty():
                command = self.queue.get()
                if 'servo_info' in command:
                    self.servo_info = command['servo_info']

    def run(self):
        """The method that starts the server and accepts connections"""

        thread = threading.Thread(target=self.queue_reader)
        thread.start()

        print("Starting server")
        self.socket.bind(("00:1A:7D:DA:71:12", self.port))
        self.socket.listen(5) # Max 5 clients, not port

        while True:
            client, address = self.socket.accept()
            client.settimeout(60)
            worker = threading.Thread(target=self.worker, args=(client, address))
            self.workers.append(worker)
            worker.start()
        
    def close(self):
        self.socket.close()

    def worker(self, client, address):
        """The worker method that handles the connection form the client, each one runs in a seperate thread"""
        size = 1024
        print("Client %s connected" % address[0])

        data = ""
        while True:
            try:
                # Because most clients streams the data rather than send it all at once, the commands needs to be split at a line ending 
                # Multiple commands can be send at once, therefor this loop
                data = data + client.recv(size)
                while True:
                    end = data.find('\n')
                    if end == -1:
                        break
                    
                    command = data[:end]
                    split = command.split(":")
                    print(split)
                    if len(split) != 0:
                        if split[0] != 'ping':
                            self.execute(client, split)
                    data = data[end+1:] # A half command can exist after send(1024) from the client, so we still need to keep this information

            except Exception as ex:
                client.close()
                print("Client %s disconnected" % address[0])
                print(ex)
                traceback.print_exc()
                return False

    def execute(self, client, commands):
        if commands[0] == 'servo_info':
            if self.servo_info is None:
                return
            print('Sending: '+ self.servo_info)
            client.send(self.servo_info + '\n')
        elif commands[0] == 'motion_state':
            self.main_queue.put({'motion_state': commands[1]})
        
#!/usr/bin/python3
 
import socket
from socket import timeout
import threading
import json
import select

from time import sleep
from random import randint


class serverThread (threading.Thread):
	def __init__(self, threadID, name, legs, servos):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.legs = legs
		self.servos = servos
		self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
                self.stopSign = False
	def run(self):
		self.s_print ("Starting... ")
		if self.name == "debugApp":
                        self.startDebugAppServer()
                elif self.name == "controller":
                        self.startControllerServer()
	def stop(self):
                print "Trying to close socket...",
		try:
                        self.stopSign = True
                        self.socket.shutdown(1)
                        self.socket.close()
                        self.s_print ("Socket closed")
                except Exception as ex:
                        self.s_print (ex)
        def bind_and_listen(self, MAC, PORT, reuse_addr=True):
                from socket import SOL_SOCKET, SO_REUSEADDR, error

                hostMACAddress = MAC # The MAC address of a Bluetooth adapter on the server. The server might ha$
		port = PORT # 3 is an arbitrary choice. However, it must match the port used by the client.
		backlog = 1
                
                if reuse_addr:
                        try:
                            self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, self.socket.getsockopt(SOL_SOCKET, SO_REUSEADDR) | 1)
                        except error:
                            pass
                self.socket.bind((hostMACAddress,port))
                self.socket.listen(backlog)

	def startDebugAppServer2(self):
                #bind a server port to listen for incoming connections
                self.bind_and_listen('00:1A:7D:DA:71:12', 3)

		while self.stopSign == False:
			try:
                                self.s_print("Waiting for a connection...")
				client, address = self.socket.accept()
				self.s_print("Connection accepted")

				while 1:
					data = ""
					# battery value
					data += str(randint(0,100)) + ";"

					# inclination value
					data += str(randint(0,100)) + ";"

					# servo values : 0 =  temperature, 1 = angle
					for x in range (1,19):
						info = "0,0;"
						for servo in self.servos:
							if str(servo.id) == str(x):
								info = "%s,%s;" % (str(servo.getTemperature()), str(servo.getAngle()))
								break

						data += info

					client.send(data.encode())

					sleep(1)

			except KeyboardInterrupt:
				self.s_print("Interrupted by user")
				if client != None:
                                        client.close()
				self.socket.close()
			except Exception as ex:
                                self.s_print(str(str(ex)[:7]))
                                if str(str(ex)[:7]) in "Timeout":
                                        self.s_print("Exception: " + str(ex))
                                        pass

				self.s_print("Closing socket with exception" + str(ex))
				if client != None:
                                        client.close()
				self.socket.close()
				break

	def startDebugAppServer(self):
                #bind a server port to listen for incoming connections
                self.bind_and_listen('00:1A:7D:DA:71:12', 3)

		while self.stopSign == False:
			try:
                                self.s_print("Hey ritseart, Waiting for a connection...")
				client, address = self.socket.accept()
				self.s_print("Connection accepted")

				while 1:
				    data = str(client.recv(1024))

                                    for leg in self.legs:
                                        leg.taskList.put(data)
                                    """if data == "f":
                                        for leg in self.legs:
                                            leg.taskList.put("f")
                                            
                                    
                                    elif data == "b":
                                        for leg in self.legs:
                                            leg.taskList.put("b")
                                            
				    elif data == "idle":
                                        for leg in self.legs:
                                            leg.taskList.put("idle")"""
                                            
				    print("data:" + data)

			except KeyboardInterrupt:
				self.s_print("Interrupted by user")
				if client != None:
                                        client.close()
				self.socket.close()
			except Exception as ex:
                                self.s_print(str(str(ex)[:7]))
                                if str(str(ex)[:7]) in "Timeout":
                                        self.s_print("Exception: " + str(ex))
                                        pass

				self.s_print("Closing socket with exception" + str(ex))
				if client != None:
                                        client.close()
				self.socket.close()
				break

        def startControllerServer(self):
            #bind a server port to listen for incoming connections
            #self.bind_and_listen('00:1A:7D:DA:71:12', 1)
            self.socket.settimeout(2)
            self.socket.setblocking(0)
            serverMACAddress = '98:D3:31:FD:17:0D'
            
            while self.stopSign == False:
                try:                                
                    while True:
                        try:
                            self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
                            self.s_print("Trying to connect")                                         
                            self.socket.connect((serverMACAddress,1))
                            self.s_print(self.socket)                                      
                            break
                        except Exception as ex:
                            print(str(ex))
                            self.s_print("Failed to connect")
                            sleep(4)
                
                    self.s_print("Connected")         
                    
                    aantal=0
                    error=0
                    data = ""
                    while True:
                        sleep(.2)
                        data_end = -1
                        self.socket.send("1")
                        try:
                            while data_end == -1:

                                try:                                                                
                                    print "trying to receive..."
                                    data += self.socket.recv(1024)
                                    print(str(data))  
                                    #print(data)
                                    #if data[0] == "0":                                           
                                    #        print("Values")
                                    #elif data[0] == "1":
                                    #        print("Pop balloon")
                                    #elif data[0] == "2":
                                    #        print("Pick up egg")
                                    #elif data[0] == "3":
                                    #        print("Dance")
                                    #elif data[0] == "4":
                                    #        print("Quit connection")
                                
                                except:
                                    if error==1:
                                        error_start = True
                                        print(error)
                                        break
                                    else:
                                        error_start = False
                                        break
                                    if error_start == True and error >= 10 or error >= 20 or eroor >= 30 or error >=40 or eroor >=50:
                                        print "Error count" + error
                                    error += 1
                                    break

                                data_end = data.find('\n')

                                if data_end != -1:
                                    rec = data[:data_end]
                                    try:
                                        data_json = rec
                                        load_json = json.loads(data_json)
                                        #Dit zijn de programma/races van de smartconroller
                                        programma1 = load_json["programma1"]
                                        programma2 = load_json["programma2"]
                                        print programma1
                                        print programma2

                                        aantal = aantal + 1
                                        data = ""
                                    except(ValueError, KeyError, TypeError):
                                        print("JSON format error")
                                        self.socket.close()
                                        time.sleep(1)
                                    rec = rec[data_end+1:]

                        except KeyboardInterrupt:
                            self.s_print("keyboardInterrupt")
                        except socket.timeout:
                            self.s_print("socket timeout")
                        except socket.error:
                            self.s_print("socket error")
                        except Exception as ex:
                            print("Failed to receive: " + str(ex))

                except KeyboardInterrupt:
                    self.s_print("Interrupted by user")
                    self.socket.close()
                except Exception as ex:
                    if str(ex)[:7] not in "Timeout":
                        self.s_print("timeout")
                    self.s_print("Closing socket with exception" + str(ex))
                    self.socket.close()
                    break
                                


        
        def s_print(self, message):
                 print("[" + self.name + "] " + str(message)) 
			

			
				

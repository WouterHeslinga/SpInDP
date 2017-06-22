import socket
import threading

sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("00:1A:7D:DA:71:12", 1))
sock.listen(5) # Max 5 clients, not port

def worker(client, address):
    print(("Client connectend: " +  str(address)))
    try:
        while True:
            data = client.recv(1024)
            print(data)
            client.send(data)
    except:
        print("Bang Bang Bang: " + str(address))
        client.close()

workers = []
print("Awaiting connection")

try:
    while True:
        client, address = sock.accept()
        client.settimeout(60)
        workert = threading.Thread(target=worker, args=(client, address))
        workers.append(workert)
        workert.start()
except KeyboardInterrupt:
    sock.close()
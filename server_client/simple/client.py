import socket
import time

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    time.sleep(2)
    send_content = input("Please input :")
    # str to bytes
    send_content = str.encode(send_content)
    sock.send(send_content)
    print(sock.recv(1024))
    sock.close()



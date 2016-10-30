import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8001))
time.sleep(2)
send_content = b'1'
sock.send(send_content)
print(sock.recv(1024))
sock.close()



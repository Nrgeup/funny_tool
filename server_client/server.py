import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8001))
sock.listen(5)  # Begin to listen
while True:
    connection, address = sock.accept()
    try:
        connection.settimeout(5)
        buf = connection.recv(1024)
        if buf == b'1':
            connection.send(b'welcome to server!')
        else:
            connection.send(b'please go out!')
    except socket.timeout:
        print("Time out")
    connection.close()


import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 10101)
sock.bind(addr)
sock.listen(5)
while True:
    (connectedSock,clientAddress) = sock.accept()
    msg = connectedSock.recv(1024).decode()
    msg = "Here's the data" + msg
    connectedSock.sendall(msg.encode())


import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 10101)
sock.connect(address)

i = 0

for i in range(0,100):
    socket.sendall(i.str.encode())
    reply = socket.recv(1024)
    print(reply)




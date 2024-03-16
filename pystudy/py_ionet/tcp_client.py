"""
客户端套接字
"""
import socket

socketfd = socket.socket()

server_addr = ('127.0.0.1', 8888)
socketfd.connect(server_addr)

while True:
    msg = input('>>')
    socketfd.send(msg.encode())
    if msg == '##':
        print('client exit')
        break
    data = socketfd.recv(1024)
    print('From server:', data.decode())

socketfd.close()

"""
tcp服务端流程
"""

import socket

# 创建TCP套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 异常重启后快速释放地址，必须在绑定之前
sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定地址
sockfd.bind(('127.0.0.1', 8888))

# 设置监听
sockfd.listen(3)

while True:
    print("waiting for connect ...")
    try:
        connfd, addr = sockfd.accept()
        print("connect from:", addr)
    except KeyboardInterrupt:
        print('Server exit')
        break

    while True:
        try:
            data = connfd.recv(1024)
        except :
            print('Client Unexpected interruption')
            break
        if data == b'##':
            """接收的为字节串"""
            print("client exit")
            break
        print("receive:", data.decode())
        n = connfd.send(b'thanks')
        print('send %d bytes' % n)
    connfd.close()

sockfd.close()

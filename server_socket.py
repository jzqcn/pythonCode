#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket,time,threading

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    print("\n")
    sock.send(b'Server: hello Welcome!')
    while True:
        recv_data = ''
        try:
            recv_data = sock.recv(2048)
        except Exception as err:
            print("一个客户端关闭了 ",err)
            break
        time.sleep(0.1)
        if not recv_data or recv_data.decode('utf-8') == 'exit':
            break

        print(recv_data.decode('utf-8'))
        sock.send(('server:%s!' % recv_data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('127.0.0.1', 9998))

serverSocket.listen(5)

print('Waiting for connection...')

while True:
    # 接受一个新连接:
    sock, addr = serverSocket.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
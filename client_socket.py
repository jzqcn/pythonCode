#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket,time,threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
client_socket.connect(('127.0.0.1', 9001))
# 接收欢迎消息:
#print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))cls
client_socket.send(b'hello i am client ')

# print("循环发送==============")
# while True:
#     time.sleep(1)
#     client_socket.send(b'hello i am client ')

print("开始循环==============")
while True:
    recv_data = ''
    try:
        recv_data = client_socket.recv(1024)
    except Exception as err:
        print("服务端关闭了 ",err)
        break
    
    print("接收的数据: ",recv_data.decode('utf-8'))
    time.sleep(0.1)
    if not recv_data or recv_data.decode('utf-8') == 'exit':
        print("没有接受到数据 或 exit 退出")
        break

    outData = input("请输入要文字：")
    client_socket.send(('%s'% outData).encode('utf-8'))
    if outData == "exit":
        break

client_socket.close()
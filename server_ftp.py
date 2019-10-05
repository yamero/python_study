#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket,os,threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9998))
s.listen(5)

def client_handle(sock, addr):
    while True:
        client_data = sock.recv(1024).decode()
        if not client_data or client_data == 'exit':
            break
        cmd, filename = client_data.split()
        if os.path.isfile(filename):
            sock.send(b'yes')
            sock.recv(1024)
            f = open(filename, 'rb')
            file_size = os.stat(filename).st_size
            sock.send(str(file_size).encode())
            print('开始发送文件')
            for file_content in f:
                sock.send(file_content)
            print('文件已成功发送')
            f.close()
        else:
            sock.send('您要下载的文件不存在'.encode())
            print('用户要下载的文件不存在')
    sock.close()

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=client_handle, args=(sock, addr))
    t.start()
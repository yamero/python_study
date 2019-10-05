#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9998))

while True:
    cmd = input('请输入要下载的文件名：')
    if cmd.startswith('get'):
        s.send(cmd.encode())
        prefix, filename = cmd.split()
        server_res = s.recv(1024).decode()
        if server_res == 'yes':
            s.send(b'yes')
        else:
            print(server_res)
            continue
        file_size = int(s.recv(1024).decode())
        received_size = 0
        f = open(filename + '.new', 'wb')
        while received_size < file_size:
            file_content = s.recv(1024)
            f.write(file_content)
            received_size += len(file_content)
        f.close()
        print('文件下载完毕')
    else:
        break
s.close()

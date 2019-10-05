import socket,threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('等待客户端连接')

def tcplink(sock, addr):
    print('客户端 %s %s 已连接' % addr)
    sock.send('欢迎使用黎昕ftp1.0'.encode())
    while True:
        data = sock.recv(1024).decode()
        if not data or data == 'exit':
            break
        sock.send(('你说：%s' % data).encode())
    sock.close()
    print('客户端 %s %s 已断开' % addr)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

data = s.recv(1024).decode()
print(data)

while True:
    msg = input('请输入想说的话：')
    if not msg or msg == 'exit':
        break
    s.send(msg.encode())
    data = s.recv(1024).decode()
    print(data)
s.close()
import socket

# КЛИЕНТСКИЙ
# содаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))

# for serverBig.py
s.send(b'Hello.\n')

# for server.py
# s.send(b'Hello.')

print(s.recv(1024))
s.close()

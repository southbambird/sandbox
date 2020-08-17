import socket

SERVER_ADDR = "127.0.0.1"
SERVER_PORT = 12345

s = socket.socket()

print('connect to server...\n')
s.connect((SERVER_ADDR,SERVER_PORT))
print('connected.')

print('receive message:')
while (res := s.recv(1024)) != b'':
    print(res.decode())
print('end')

s.shutdown(socket.SHUT_RDWR)
s.close()
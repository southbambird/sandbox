import socket
import os

HOST = ''
PORT = 12345

s = socket.socket()

s.bind((HOST, PORT))

s.listen(5)

print('listen... ')

while True:
    print('wait connection...')

    client = s.accept()
    client_socket = client[0]

    if(os.fork() == 0):
        s.close()

        client_socket.send(b'Sending a message!!')
        print('send done.')

        client_socket.close()
        print('connected socket close.')
    
        exit(0)
    
    client_socket.close()
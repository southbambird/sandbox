#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 50000

sock.bind(((host, port)))
sock.listen(1)

print('Waiting connection ...')

connection, addr = sock.accept()
print('Connection from: ' + str(addr))

while True:
    data = connection.recv(1024)

    if data == b'exit':
        break

    print('Received a message: ' + str(data))

    connection.send(data)
    print('Sent a message: ' + str(data))

connection.close()
sock.close()

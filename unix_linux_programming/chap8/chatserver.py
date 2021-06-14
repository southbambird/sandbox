import socket
import select

SERVER_PORT = 12345
NQUEUESIZE  = 5
MAXNCLIENTS = 10

client_list = list()

def sorry(client: socket.socket):
    client.send(b"Sorry, it's full.")

def delete_client(client: socket.socket, client_list: list):
    for s in client_list:
        if s == client:
            client_list.remove(client)

def talks(talks_socket: socket.socket):
    c = ''
    while c != b'\n':
        c = talks_socket.recv(1024)
        if c.decode() == '':
            talks_socket.shutdown(socket.SHUT_RDWR)
            talks_socket.close()
            delete_client(talks_socket, client_list)
            print('connection closed.')
            return
        for client in client_list:
            client.send(c)

def main():
    s = socket.socket()
    s.bind((socket.INADDR_ANY,SERVER_PORT))
    s.listen()

    print('Ready...\n')

    while True:
        socket.
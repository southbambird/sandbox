import os
BUF_SIZE = 5

try:
    fd = os.open('hello.txt',os.O_RDONLY)
    buf = os.read(fd,BUF_SIZE)
    print(buf.decode())
except OSError as err:
    print(err)


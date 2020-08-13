import os

try:
    fd = os.open("bye.txt",os.O_WRONLY)
    os.write(fd, b'See you')
    os.write(fd, b' later!')
    os.write(fd, b'\nBye!\n')
    os.close(fd)
except OSError as err:
    print(err)
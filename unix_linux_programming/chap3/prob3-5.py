import os
import sys
BUF_SIZE = 1024
try:
    input_fd = os.open("input.txt",os.O_RDONLY)

    while((buf := os.read(input_fd,BUF_SIZE)) != b''):
        os.write(sys.stdout.fileno(),buf)

    os.close(input_fd)

except OSError as err:
    print(err)
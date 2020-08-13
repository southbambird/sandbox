import os
import sys
BUF_SIZE = 1024
try:
    output_fd = os.open("output_writeout.txt",os.O_WRONLY | os.O_TRUNC | os.O_CREAT, 0o666)

    while((buf := os.read(sys.stdin.fileno(),BUF_SIZE)) != b''):
        os.write(output_fd,buf)

    os.close(output_fd)

except OSError as err:
    print(err)
import os

try:
    input_fd = os.open("input.txt",os.O_RDONLY)
    print(os.lseek(input_fd,10,os.SEEK_SET))
    print(os.read(input_fd,5).decode())
    print(os.lseek(input_fd,0,os.SEEK_CUR))
except OSError as err:
    print(err)
import os

if (fd := os.open('empty.file', os.O_WRONLY| os.O_CREAT | os.O_TRUNC, 0o666)) == -1:
    print('error')
    exit(-1)

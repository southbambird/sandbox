import os
BUF_SIZE = 1024
try:
    input_fd = os.open("input.txt",os.O_RDONLY)
    output_fd = os.open("output.txt",os.O_WRONLY | os.O_TRUNC | os.O_CREAT, 0o666)

    while((buf := os.read(input_fd,BUF_SIZE)) != b''):
        os.write(output_fd,buf)

    os.close(input_fd)
    os.close(output_fd)

except OSError as err:
    print(err)
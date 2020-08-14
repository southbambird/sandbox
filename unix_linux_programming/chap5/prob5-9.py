import os
import time

cmd = input('@ ')
if os.fork() == 0:
    os.execlp(cmd,cmd)
    print('execute failed')
    os._exit(-1)


status = os.wait()
if not os.WIFEXITED(status[1]):
    print('error')
    exit(-1)

print('child process pid:', status[0])
print('child process exit code: ', os.WEXITSTATUS(status[1]))
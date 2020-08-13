import os
import time

if (pid := os.fork()) == -1:
    print('error')
elif pid == 0:
    print('Child PID is ',str(os.getpid()))
    print('Parent Process PID is ', str(os.getppid()))
    exit(0)

print('Parend PID is ', str(os.getpid()))
print('Child Process PID is ', str(pid))
while True:
    time.sleep(1)
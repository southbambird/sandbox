import os
import subprocess

mypid = os.getpid()
print("My pid is {mypid}".format(mypid=mypid))

res = subprocess.check_output(['ps', '-l', '-e', str(mypid)])
print(res.decode())

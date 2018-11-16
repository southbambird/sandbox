string = input()
array = string.split(' ')
N = int(array[0])
K = int(array[1])
if N % K == 0:
    print(0)
else:
    print(1)

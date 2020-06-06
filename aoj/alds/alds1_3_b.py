from collections import deque

queue = deque()
total_time = 0
n, q = map(int,input().split(' '))
for _ in range(n):
    name, time = input().split(' ')
    queue.append((name,int(time)))


while True:
    try:
        name, time = queue.popleft()
        if time - q <= 0:
            total_time += time
            print(name,total_time,sep=' ')
        elif time - q > 0:
            total_time += q
            queue.append((name,time-q))
    except IndexError:
        break
from collections import deque

class MyDeque:
    def __init__(self):
        self.data = deque()

    def push(self, d, x):
        if d == 0:
            self.data.appendleft(x)
        elif d == 1:
            self.data.append(x)

    def random_access(self, p):
        print(self.data[p])

    def pop(self, d):
        if d == 0:
            self.data.popleft()
        elif d == 1:
            self.data.pop()

my_deque = MyDeque()
q = int(input())

for _ in range(q):
    args = input().split(' ')
    if args[0] == '0':
        d = int(args[1])
        x = int(args[2])
        my_deque.push(d, x)

    elif args[0] == '1':
        p = int(args[1])
        my_deque.random_access(p)

    elif args[0] == '2':
        d = int(args[1])
        my_deque.pop(d)

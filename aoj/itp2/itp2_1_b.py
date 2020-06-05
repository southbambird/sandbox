from array import array

class Deque:
    def __init__(self):
        self.vec = array('l')
    
    def push(self, d, x):
        if d == 0:
            self.vec.insert(0, x)
        elif d == 1:
            self.vec.append(x)
    
    def randomAccess(self, p):
        print(self.vec[p])
    
    def pop(self, d):
        if d == 0:
            self.vec.pop(0)
        elif d == 1:
            self.vec.pop()

if __name__ == '__main__':
    deque = Deque()

    n = int(input())
    for _ in range(n):
        args = input().split(' ')
        ope = args[0]
        if ope == '0':
            d = int(args[1])
            x = int(args[2])
            deque.push(d,x)
        elif ope == '1':
            p = int(args[1])
            deque.randomAccess(p)
        elif ope == '2':
            d = int(args[1])
            deque.pop(d)



class Vector:
    def __init__(self):
        self.vec = []
    
    def push_back(self,x):
        self.vec.append(x)
    
    def random_access(self,p):
        return self.vec[p]

    def pop_back(self):
        self.vec.pop()

my_vec = Vector()

n = int(input())
for _ in range(n):
    args = input().split(' ')
    ope = args[0]
    if ope == '0':
        my_vec.push_back(int(args[1]))
    elif ope == '1':
        print(my_vec.random_access(int(args[1])))
    elif ope == '2':
        my_vec.pop_back()

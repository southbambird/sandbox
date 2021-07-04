def func(i: int, w: int, a: list) -> bool:
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    
    if func(i-1, w, a):
        return True
    
    if func(i-1, w-a[i-1], a):
        return True
    
    return False

N: int = int(input("N:"))
W: int = int(input("W:"))
a: list = list()

for i in range(N):
    a.append(int(input("a[%d]:" % i)))

if func(N, W, a):
    print("Yes!!")
else:
    print("No...")

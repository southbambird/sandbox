def func(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return func(n-1) + func(n-2) + func(n-3)

N = int(input("N:"))
for i in range(N):
    print(func(i))
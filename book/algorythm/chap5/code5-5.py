def chmin(a:int, b:int) -> int:
    if a > b:
        return b
    else:
        return a

N = int(input("N:"))
h = list()
for i in range(N):
    h.append(int(input("h[%d]:" % i)))

def rec(i: int) -> int:
    if i == 0:
        return 0
    
    res = 1000000

    res = chmin(res, rec(i - 1) + abs(h[i] - h[i-1]))

    if i > 1:
        res = chmin(res, rec(i - 2) + abs(h[i] - h[i-2]))
    
    return res

print(rec(N-1))
a = list(map(int,input().split(' ')))
n = len(a)
m = int(input())

def solve(i, m):
    if m == 0:
        return True
    elif i >= n:
        return False
    ret = solve(i+1, m) or solve(i+1, m-a[i])
    return ret

finded = solve(0, 8)
if finded:
    print('Finded!')
else:
    print('Not finded!')
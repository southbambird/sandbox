n = int(input())
a = list(map(int,input().split(' ')))
q = int(input())
m = list(map(int,input().split(' ')))

def solve(i, m):
    if(m == 0):
        return True
    elif(i >= n):
        return False
    ret = solve(i+1, m) or solve(i+1, m-a[i])
    return ret

for num in m:
    if solve(0, num):
        print('yes')
    else:
        print('no')

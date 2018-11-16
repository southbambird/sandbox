import sys
N = int(input())
for i in range(int(N/4) + 1):
    amount = i * 4
    for j in range(int(N/7) + 1):
        if(j == 0):
            pass
        else:
            amount += 7
        if(amount == N):
            print('Yes')
            sys.exit()
print('No')

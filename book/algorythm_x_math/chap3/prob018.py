n = int(input())
ary = list(map(int,input().split()))

counter = {100: 0, 200: 0, 300: 0, 400: 0}

for item in ary:
    counter[item] += 1

case1 = counter[100] * counter[400]
case2 = counter[200] * counter[300]
print(case1 + case2)

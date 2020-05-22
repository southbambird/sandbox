n, a, b = map(int,input().split(' '))
total = 0
for num in range(1,n+1):
    split_nums = [int(s) for s in list(str(num))]
    sum = 0
    for s in split_nums:
        sum += s
    if a <= sum and sum <= b:
        total += num
print(total)
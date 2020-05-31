def max_digit(a,b):
    return max(len(str(a)),len(str(b)))

n = int(input())
min = n

# O(n)で10^10なので時間的に無理
for a in range(1,n+1):
    b = n/a
    if not b.is_integer():
        continue
    num = max_digit(a, int(b))
    if num < min:
        min = num
print(min)
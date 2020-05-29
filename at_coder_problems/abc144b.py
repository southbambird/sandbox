n = int(input())
finded = False
for i in range(1,10):
    num = n / i
    if num.is_integer() and num < 10:
        print('Yes')
        finded = True
        break
if not finded:
    print('No')

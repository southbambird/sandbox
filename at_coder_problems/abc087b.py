a = int(input())
b = int(input())
c = int(input())
x = int(input())

pair_num = 0
for a_i in range(a+1):
    for b_i in range(b+1):
        for c_i in range(c+1):
            if (500*a_i + 100*b_i + 50*c_i) == x:
                pair_num += 1

print(pair_num)
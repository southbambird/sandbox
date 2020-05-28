n, l, t = map(int,input().split(' '))
ants_list = []
for i in range(n):
    x, w = map(int,input().split(' '))
    ants_list.append((x, w))

for x, w in ants_list:
    if w == 1:
        print((x+t)%l)
    elif w == 2:
        if (x-t) < 0:
            print(l+(x-t))
        else:
            print((x-t))

n, y = map(int,input().split(' '))

finded = False
for sen in range(n+1):
    for gosen in range(n+1-sen):
        if 1000*sen + 5000*gosen + 10000*(n-sen-gosen) == y:
            print(n-sen-gosen,gosen,sen,sep=' ')
            finded = True
            break
    if finded:
        break

if not finded:
    print('-1 -1 -1')


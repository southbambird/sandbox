x, y = map(int,input().split(' '))

# 以下は時間がかかりすぎる
#d = min(x, y)
#for i in range(d,0,-1):
#    if x % i == 0 and y % i == 0:
#        print(i)
#           finded = True
#        break

# ユークリッド互除法
def gcd(x, y):
    new_x = max(x, y)
    new_y = min(x, y)
    while new_y > 0:
        r = new_x % new_y
        new_x = new_y
        new_y = r
    return new_x

print(gcd(x, y))

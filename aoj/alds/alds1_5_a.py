n = 5
s = []

def make_combination():
    for i in range(n):
        s.append(0)
    rec(0)

def rec(i):
    if i == n:
        print(s)
        return 
    rec(i + 1)
    print(i)
    s[i] = 1
    rec(i + 1)
    s[i] = 0

make_combination()
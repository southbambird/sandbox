N: int = int(input("N:"))
W: int = int(input("W:"))

a = list()

for i in range(N):
    a.append(int(input("a[%d]:" % i)))

exist: bool = False

for bit in range(1 << N):
    sum: int = 0
    for a_i in range(N):
        if bit & (1 << a_i):
            sum = sum + a[a_i]
    if sum == W:
        exist = True

if exist:
    print("Yes!")
else:
    print("No...")

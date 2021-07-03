N = int(input("N:"))
v = int(input("v:"))

a = list()

for i in range(N):
    a.append(int(input("a[%d]" % (i))))

exist: bool = False
for i in range(N):
    if(a[i] == v):
        exist = True

if exist:
    print("Yes!")
else:
    print("No...")
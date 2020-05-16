from array import array

ary = array('l')

while True:
    n = input()
    if n:
        ary.append(int(n))
    else:
        break

sorted_ary = sorted(ary)

for n in sorted_ary:
    print(n)


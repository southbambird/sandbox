def gcd(m: int, n: int) -> int:
    print("m:%d n:%d" % (m, n))
    r = m % n
    if r == 0:
        return n
    return gcd(n, r)

print(gcd(51, 15))
print(gcd(15, 51))
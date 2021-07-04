def fibo(n: int) -> int:
    print("fibo(%d) called." % n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    result = fibo(n-1) + fibo(n-2)
    print("fibo(%d) = %d" % (n, result))
    return result

print(fibo(8))
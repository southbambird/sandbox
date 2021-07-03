def func(N: int) -> int:
    print("func(%d) を呼び出しました。" % N)

    if N == 0:
        return 0
    result = N + func(N-1)

    print("%d までの和 = %d" % (N,result))

    return result

func(5)
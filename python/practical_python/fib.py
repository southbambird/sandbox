import sys

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + a
    else:
        return a

def main():
    n = int(sys.argv[1])
    print(fibonacci(n))

if __name__ == "__main__":
    main()

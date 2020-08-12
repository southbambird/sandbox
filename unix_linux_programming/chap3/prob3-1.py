try:
    with open('input.txt', 'r') as f:
        print(f.fileno())

except OSError:
    print("can't open file.")
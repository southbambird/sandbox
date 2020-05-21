_ = input()
numbers = list(map(int,input().split(' ')))

count = 0
finished = False
while True:
    for index, value in enumerate(numbers):
        if value % 2 == 0:
            numbers[index] = value / 2
        else:
            finished = True
            break
    if finished:
        break
    else:
        count += 1
print(count)
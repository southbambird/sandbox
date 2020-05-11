def do_something(input):
    return input * 2

def count_str(input, counter):
    counter[input] = counter[input] + 1

counter = list(0)
for c in input():
    count_str(c,counter)
print(counter)


result = [do_something(c) for c in input()]
print(result)

map(do_something, input())


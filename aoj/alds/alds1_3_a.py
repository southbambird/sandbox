args = input().split(' ')
stack = []
for arg in args:
    if arg.isdecimal():
        stack.append(int(arg))
    elif arg == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif arg == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif arg == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
print(stack.pop())
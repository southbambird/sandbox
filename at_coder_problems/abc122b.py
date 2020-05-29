s = input()
acgt = ['A','C','G','T']
i = 0
max = 0
count = 0

while i < len(s):
    if s[i] in acgt:
        count+=1
        if count > max:
            max = count
    else:
        count = 0
    i+=1

print(max)
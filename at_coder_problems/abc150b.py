n = int(input())
s = input()
i = 0
count = 0

while i < len(s):
    if not (s[i] == 'A'):
        i+=1
        continue

    i+=1
    if not i < len(s):
        break
    if not (s[i] == 'B'):
        continue

    i+=1
    if not i < len(s):
        break
    if not (s[i] == 'C'):
        continue

    i+=1
    count+=1

print(count)
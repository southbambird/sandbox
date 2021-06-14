n = int(input())
v = int(input())
found_id = -1
for i in range(n):
    if int(input()) == v:
        found_id = i

print(found_id)

N = int(input())
A = list(map(int,input().split()))

counter = {1: 0, 2: 0, 3: 0}

for item in A:
    counter[item] += 1

case_x = (counter[1] * (counter[1] - 1)) / 2
case_y = (counter[2] * (counter[2] - 1)) / 2
case_z = (counter[3] * (counter[3] - 1)) / 2
print(int(case_x + case_y + case_z))
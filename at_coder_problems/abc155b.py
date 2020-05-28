n = int(input())
num_list = map(int,input().split(' '))
even_num_list = filter(lambda x : x % 2 == 0,num_list)

denied = False
for num in even_num_list:
    if num % 3 == 0 or num % 5 == 0:
        continue
    else:
        denied = True
        print('DENIED')
        break

if not denied:
    print('APPROVED')
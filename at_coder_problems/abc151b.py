n, k, m = map(int, input().split(' '))
score_list = map(int, input().split(' '))

must_score = n * m
for score in score_list:
    must_score -= score

if must_score <= k:
    if must_score <= 0:
        print('0')
    else:
        print(must_score)
else:
    print('-1')
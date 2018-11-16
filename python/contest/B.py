import sys

S = list(input())
if S[0] != 'A':
    print('WA')
    sys.exit()

S_aida = S[2:-1]
if S_aida.count("C") != 1:
    print('WA')
    sys.exit()

S.pop(0)
S.pop(S.index('C'))

for string in S:
    if not string.islower():
        print('WA')
        sys.exit()

print('AC')

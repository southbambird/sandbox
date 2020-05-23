n = int(input())
cards = map(int, input().split(' '))
sorted_cards = sorted(cards,reverse=True)

alice_sum = 0
bob_sum = 0
for i in range(n):
    if i % 2 == 0:
        alice_sum += sorted_cards[i]
    else:
        bob_sum += sorted_cards[i]

print(alice_sum - bob_sum)
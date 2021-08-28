counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}

key = 'wheat'

# bad1
if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1

# bad2
try:
    count = counters[key]
except KeyError:
    count = 0

counters[key] = count + 1

# good
count = counters.get(key, 0)
counters[key] = count + 1

votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}

key = 'brioche'
who = 'Elmer'

# bad1
if key in votes: 
    names = votes[key]
else:
    votes[key] = names = []

names.append(who)
print(votes)

# bad2
try:
    names = votes[key]
except KeyError:
    votes[key] = names = []

names.append(who)
print(votes)

#good
names = votes.get(key)
if names is None:
    votes[key] = names = []

names.append(who)

#good2
if (names := votes.get(key)) is None:
    votes[key] = names = []

names.append(who)

#簡潔だがsetdefaultが混乱する
names = votes.setdefault(key,[])
names.append(who)

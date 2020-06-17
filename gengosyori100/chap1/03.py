moji = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

counter = {}
for chr in moji:
    if chr == ' ':
        continue
    try:
        counter[chr] += 1 
    except KeyError:
        counter[chr] = 1

print(sorted(counter.items(),key=lambda x:x[1], reverse=True))
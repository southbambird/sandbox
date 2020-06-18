def n_gram(target, n):
    return [ target[i:i+n] for i in range(len(target) - n + 1)]

str1 = "paraparaparadise"
str2 = "paragraph"

x = set(n_gram(str1, 2))
y = set(n_gram(str2, 2))

print(x | y)

print(x & y)

print(x - y)

if "se" in x & y:
    print("Yes")
else:
    print("No")
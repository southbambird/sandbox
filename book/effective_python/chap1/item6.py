snack_calories = {
    'chips': 140,
    'popcorn': 80,
    'nuts': 190,
}
items = tuple(snack_calories.items())
print(items)

item = ('Peanut butter', 'Jelly')
first = item[0]
second = item[1]
print(first, 'and', second)

# pair = ('Chocolate', 'Peanut butter')
# pair[0] = 'Honey'

item = ('Peanut butter', 'Jelly')
first, second = item
print(first, 'and', second)

favorite_snacks = {
    'salty': ('pretzels', 100),
    'sweet': ('cookies', 180),
    'veggie': ('carrots', 20),
}

((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items()

print(f'Favorite {type1} is {name1} with {cals1} calories')
print(f'Favorite {type2} is {name2} with {cals2} calories')
print(f'Favorite {type3} is {name3} with {cals3} calories')

print(type(favorite_snacks))
print(type(favorite_snacks.items()))

print(favorite_snacks)
print(favorite_snacks.items())


snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
# bad
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i+1}: {name} has {calories} calories')

# good
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} has {calories} calories')
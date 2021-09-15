stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']

def get_batches(count, size):
    return count // size

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)
# good
found = {name: get_batches(stock.get(name, 0), 8)
        for name in order
        if get_batches(stock.get(name, 0), 8)}
print(found)

# more good
found2 = {name: batches for name in order
        if (batches := get_batches(stock.get(name, 0), 8))}
print(found2)

#result = {name: (tenth := count // 10)
#            for name, count in stock.items() if tenth > 0}
result = {name: tenth for name, count in stock.items()
        if (tenth := count // 10) > 0}
print(result)


half = [(squared := last ** 2)
        for count in stock.values()
        if (last := count // 2) > 10]
print(f'Last item of {half} is {last} ** 2 = {squared}')
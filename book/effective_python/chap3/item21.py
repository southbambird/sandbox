def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

def sort_priority2(numbers, group):
    found = False  #scope:sort_priority2
    def helper(x):
        if x in group:
            found = True  #scope:helper
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)

def sort_priority2(numbers, group):
    found = False  #scope:sort_priority2
    def helper(x):
        nonlocal found  #add
        if x in group:
            found = True  #scope:sort_priority2
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)
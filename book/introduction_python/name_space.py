animal = 'fruitbat'

def print_global():
    print('inside print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

print('at the top level:', animal)
print_global()
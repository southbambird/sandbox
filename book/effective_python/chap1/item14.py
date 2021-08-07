numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25),
]

# error
#tools.sort()

print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted:  ', tools)


places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('Case sensitive:  ', places)
places.sort(key=lambda x: x.lower())
print('Case insensitive:', places)

power_tools = [
    Tool('drill', 4),
    Tool('cicular saw', 5), 
    Tool('jackammer', 40),
    Tool('sander', 4),
]

saw = (5, 'circular saw')
jackhammer = (40, 'jackhammer')
assert not (jackhammer < saw)

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)
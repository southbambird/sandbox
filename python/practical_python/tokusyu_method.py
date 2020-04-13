class A:
    def __len__(self):
        return 5

a = A()
print(len(a))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __setattr__(self, name, value):
        if name not in ('x', 'y'):
            raise AttributeError('Not allowed')
        super().__setattr__(name, value)
    def __delattr__(self, name):
        if name in ('x', 'y'):
            raise AttributeError('Not allowed')
        super().__delattr__(name)

p = Point(1, 2)
print(p.__repr__())
print(p)

# p.z = 3
p.x = 3
print(p.x)


class QueryParams:
    def __init__(self, params):
        self.params = params
    def __bool__(self):
        return bool(self.params)
    def __len__(self):
        return len(self.params)

query = QueryParams({})
print(bool(query))

query = QueryParams({'key': 'value'})
print(bool(query))



class Adder:
    def __init__(self):
        self._values = []
    def add(self, x):
        self._values.append(x)
    def __call__(self):
        return sum(self._values)

adder = Adder()
adder.add(1)
adder.add(3)
print(adder())
adder.add(5)
print(adder())





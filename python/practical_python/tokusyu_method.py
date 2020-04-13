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
p = Point(1, 2)
print(p.__repr__())
print(p)

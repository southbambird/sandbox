fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon':5,
}

def make_lemonade(count):
    ...

def out_of_stock():
    ...

if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

def slice_bananas(count):
    ...

class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    ...

pieces = 0
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()


if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()
    
#bad
def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('Invalid inputs')

x, y = 0, 5
result = careful_divide(x, y)
if not result:
    print('Invalid inputs')

#good 
def careful_divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

success, result = careful_divide(x, y)
if not success:
    print('Invalid inputs')

#bad 計算結果返した意味がない
_, result = careful_divide(x, y)
if not result:
    print('Invalid Inputs')

#best
def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')

x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print(f'Result is {result}')

def careful_divide(a: float, b: float) -> float:
    """Divides a by b.
    
    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')

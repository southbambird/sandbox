import math

def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output

def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')

def run(it):
    for output in it:
        transmit(output)

run(wave(3.0, 8))

def my_generator():
    received = yield 1
    print(f'received = {received}')

it = iter(my_generator())
output = next(it)
print(f'output = {output}')

try:
    next(it)
except StopIteration:
    pass
else:
    assert False

it = iter(my_generator())
output = it.send(None)
print(f'output = {output}')

try:
    it.send('hello!')
except StopIteration:
    pass
else:
    assert False

def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output

def run_modulating(it):
    amplitudes = [
        None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)


run_modulating(wave_modulating(12))
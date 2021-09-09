def remainder(number, divisor):
    return number % divisor

my_kwargs = {
    'number': 20,
    'divisor': 7,
}

assert remainder(**my_kwargs) == 6

def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

print_parameters(alpha=1.5, beta=9, gamma=4)



def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f'{flow:.3} kg per second')

def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
print(f'{flow_per_second:.3} kg per second')
print(f'{flow_per_hour:.3} kg per hour')

def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period
pounds_per_hour = flow_rate(weight_diff, time_diff,
                            period=3600, units_per_kg=2.2)
print(f'{pounds_per_hour:.3} kg per hour')
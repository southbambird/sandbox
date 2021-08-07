car_ages = [0, 9, 4, 8, 7,20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages,reverse=True)
#oldest, second_oldest = car_ages_descending

#bad
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

#good catch-all-unpack
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)

car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova'),
}

((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = car_inventory.items()

print(f'Best at {loc1} is {best1}, {len(rest1)} others')
print(f'Best at {loc2} is {best2}, {len(rest2)} others')

it = iter(range(1, 3))
first, second = it
print(f'{first} and {second}')
print(list(it))

def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')
    ...
#bad
all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV Header:', header)
print('Row count: ', len(rows))

#good
it = generate_csv()
header, *rows = it
print('CSV Header:', header)
print('Row count: ', len(rows))

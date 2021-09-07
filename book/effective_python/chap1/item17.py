visits = {
    'Mexico': {'Tulum', "puerto Vallarta"},
    'Japan': {'Hakone'},
}

# setdefault
visits.setdefault('France', set()).add('Arles')

# get
if (japan := visits.get('Japan')) is None:
    visits['Japan'] = japan = set()
japan.add('Kyoto')

print(visits)

#imaiti
class Visits:
    def __init__(self):
        self.data = {}
    
    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)

visits = Visits()
visits.add('Russia', 'Yekaterinburg')
visits.add('Tanzania', 'Zanzibar')
print(visits.data)

#good
from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)
    
    def add(self, country, city):
        self.data[country]. add(city)
    
visits = Visits()
visits.add('England', 'Bath')
visits.add('England', 'London')
print(visits.data)
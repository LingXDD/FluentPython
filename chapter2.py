import array
import os
from collections import namedtuple

symbols = '@#$%^'
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# Difference between List Comprehension and Generator Expression
# List Comprehension
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# Generator Expression
for tshirt in (f'({c}, {s})' for c in colors for s in sizes):
    print(tshirt)

print(tuple(ord(symbol) for symbol in symbols))

print(array.array('I', (ord(symbol) for symbol in symbols)))

# --------------------------------------------------------
# Tuple unpacking
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print(f'{passport[0]}/{passport[1]}')

divmod(20, 8)
t = (20, 8)
divmod(*t)  # The '*' operator can be used to unpack an iterable as arguments for a function, equals to divmod(20, 8)


_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
# _: '/home/luciano/.ssh'   filename: 'idrsa.pub'

# Use '*' to handle the remaining elements.
a, b, *rest = range(5)
# a, b, rest -> (0, 1, [2, 3, 4])
a, b, *rest = range(3)
# a, b, rest -> (0, 1, [2])
a, b, *rest = range(2)
# a, b, rest -> (0, 1, [])
a, *body, c, d = range(5)
# a, body, c, d -> (0, [1, 2], 3, 4)
*head, b, c, d = range(5)
# head, b, c, d -> ([0, 1], 2, 3, 4)

# Nested tuple unpacking
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi Ncr', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]
print(f'{'':15} | {'lat.':^9} | {'long.':^9}')
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# Namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139,691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)

# Namedtuple-specific attributes
print(City._fields)
# >>> ('name', 'country', 'population', 'coordinates')
Latlong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, Latlong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
# >>>{'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': Latlong(lat=28.613889, long=77.208889)}
for key, value in delhi._asdict().items():
    print(key + ':', value)
# >>>
# name: Delhi NCR
# country: IN
# population: 21.935
# coordinates: Latlong(lat=28.613889, long=77.208889)

# --------------------------------------------------------
# Slicing
s = 'bicycle'
print(s[::3])
# >>> 'bye'
print(s[::-1])
# >>> 'elcycib'
print(s[::-2])
# >>> 'eccb'

l = list(range(10))
# >>> l: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]
# >>> l: [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
# >>> l: [0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11, 22]
# >>> l: [0, 1, 20, 11, 5, 22, 9]
l[2: 5] = [100]  # l[2:5] = 100 returns Typeerror: can only assign an iterable
# >>> l: [0, 1, 100, 22, 9]

# --------------------------------------------------------
# 2.5 Using '+' and '*' on sequences
l = [1, 2, 3]
print(l * 5)
# >>> [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(5 * 'abc')
# >>> 'abcabcabcabcabc'

board = [['_'] * 3 for i in range(3)]  # weird_board = [['_'] * 3] * 3 WRONG!
# >>> board[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# --------------------------------------------------------
# 2.6 list augmented assignment
l = [1, 2, 3]
# >>> id(l) = 123456
l *= 2
# >>> id(l) = 123456
t = (1, 2, 3)
# >>> id(t) = 456789
t *= 2  # ID is changed
# >>> id(t) = 987654

t = (1, 2, [30, 40])
# t[2] += [50, 60]
# >>> t -> (1, 2, [30, 40, 50, 60]) but also a TypeError: 'tuple' object does not support item assignment
t[2].extend([50, 60])
# >>> t -> (1, 2, [30, 40, 50, 60]) and no errors


import array
import os
import bisect
import sys
import numpy
import random
from collections import namedtuple
from collections import deque
from time import perf_counter as pc

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

# --------------------------------------------------------
# 2.8 Using bisect to manage sorted sequences
# using bisect_left and bisect
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '   |'
        print(ROW_FMT.format(needle, position, offset))


if sys.argv[-1] == 'left':
    bisect_fn = bisect.bisect_left
else:
    bisect_fn = bisect.bisect

print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)


# -------------------
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


final_grade = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(final_grade)
# -------------------
# using bisect.insort
SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print(f'{new_item} ->', my_list)

# --------------------------------------------------------
# Array
floats = array.array('d', (random.random() for i in range(10**5)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array.array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**5)
fp.close()
print(floats2[-1])
print(floats2 == floats)

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
# >>> 5
print(memv[0])
# >>> -2
memv_oct = memv.cast('B')
print(memv_oct.tolist())
# >>> [255, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 4
print(numbers)
# >>> array('h', [-2, -1, 1024, 1, 2])

# -------------------
# Numpy and SciPy
a = numpy.arange(12)
print(a)
# >>> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(type(a))
# >>> <class 'numpy.ndarray'>
a.shape = 3, 4
print(a)
# >>> array([[ 0  1  2  3]
#           [ 4  5  6  7]
#           [ 8  9 10 11]])
print(a[2])
# >>> array([8  9 10 11])
print(a[2, 1])
# >>> 9
print(a[:, 1])
# >>> array([1, 5, 9])
print(a.transpose())
# >>> [[ 0  4  8]
#      [ 1  5  9]
#      [ 2  6 10]
#      [ 3  7 11]]

# floats = numpy.loadtxt('floats-10M0lines.txt')
# print(floats[-3:])
# # >>> array([3016362.69195522, 535281.10514262, 4566560.44373946])
# floats *= .5
# print(floats[-3:])
# # >>> array([1508181.34597761, 267640.55257131, 2283280.22186973])
# t0 = pc()
# floats /= 3
# pc() - t0
# # >>> 0.03690556302899495
# numpy.save('floats-10M', floats)
# floats2 = numpy.load('floats-10M.npy', 'r+')
# floats2 *= 6
# print(floats2[-3:])
# # >>> memmap([3016362.69195522, 535281.10514262, 4566560.44373946])

# -------------------
# collections.deque
dq = deque(range(10), maxlen=10)
print(dq)
# >>> deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.rotate(3)
# >>> deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.rotate(-4)
# >>> deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
dq.appendleft(-1)
# >>> deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.extend([11, 22, 33])
# >>> deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
dq.extendleft([10, 20, 30, 40])
# >>> deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)


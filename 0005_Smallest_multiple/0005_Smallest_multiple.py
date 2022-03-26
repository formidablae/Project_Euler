from functools import reduce
from math import gcd

lcm = reduce(lambda x, y: x * y // gcd(x, y), range(1, 21))
print(lcm)

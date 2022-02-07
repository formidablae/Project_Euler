# Find the sum of the digits in the number 100!
from functools import reduce

print(sum(list(map(int, str(reduce(lambda x, y: x * y, range(1, 101)))))))

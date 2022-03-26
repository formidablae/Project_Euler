from functools import reduce


def factors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


num = 1
i = 2
while True:
    num = num + i
    if len(factors(num)) > 500:
        print(num)
        break
    i = i + 1

from functools import reduce


def factors(n):
    return list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


num = 600851475143
factors = factors(num)
factors.sort(reverse=True)
for i in range(len(factors)):
    if isPrime(factors[i]):
        print(factors[i])
        break

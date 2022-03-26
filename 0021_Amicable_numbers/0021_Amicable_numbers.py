# Let d(n) be defined as the sum of proper divisors of n(numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142
# so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


from itertools import compress


def pr(n):  # primes
    """Returns  a list of primes < n for n > 2"""
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    return [2, *list(compress(range(3, n, 2), sieve[1:]))]


def f(n):  # factorization
    """Returns a list of the prime factorization of n"""
    pf = []
    for p in pr(n):
        if p * p > n:
            break
        count = 0
        while not n % p:
            n //= p
            count += 1
        if count > 0:
            pf.append((p, count))
    if n > 1:
        pf.append((n, 1))
    return pf


def d(n, exclude_n=False):  # divisors
    """Returns an unsorted list of the divisors of n"""
    divs = [1]
    for p, e in f(n):
        divs += [x * p**k for k in range(1, e + 1) for x in divs]
    if exclude_n and n in divs:
        divs.remove(n)
    return divs


def amicable(n, exclude_n=False):  # amicable numbers
    """Returns a list of the amicable numbers under n"""
    amicables = []
    for a in range(2, n):
        b = sum(d(a, exclude_n))
        if b < n and sum(d(b, exclude_n)) == a and a != b:
            amicables.append((a, b))
    return amicables


print("Proper divisors of n=220:", d(220, True))
print("Amicable pairs of numbers under 1000:", amicable(1000, True))
amicable_numbers = set()
for a, b in amicable(10000, True):
    amicable_numbers.add(a)
    amicable_numbers.add(b)
print("Set of amicable numbers under 10000:", amicable_numbers)
print("Sum of all amicable numbers under 10000:", sum(amicable_numbers))

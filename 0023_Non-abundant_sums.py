# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that
# all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though
# it is known that the greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from itertools import compress


def pr(n):  # primes
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2, *list(compress(range(3, n, 2), sieve[1:]))]


def f(n):  # factorization
    """ Returns a list of the prime factorization of n """
    pf = []
    for p in pr(n):
        if p*p > n:
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
    """ Returns an unsorted list of the divisors of n """
    divs = set([1])
    for p, e in f(n):
        divs |= set([x*p**k for k in range(1, e+1) for x in divs])
    if exclude_n and n in divs:
        divs.remove(n)
    return divs


def is_abundant(n):
    """ Returns if a number is abundant, its proper divisors """
    return sum(d(n, True)) > n


def get_all_abundant_numbers_below(n):
    """ Returns all abundant numbers under n """
    return set(filter(is_abundant, range(1, n)))


def can_sum_two_abundant(n, abundant_numbers):
    """ Returns if a number can be written as the sum of two abundant numbers """
    return any(n - a in abundant_numbers for a in abundant_numbers)


all_abundant_numbers = get_all_abundant_numbers_below(28123)
sum_non_abundant = sum([x for x in range(1, 28123) if not can_sum_two_abundant(x, all_abundant_numbers)])
print(sum_non_abundant)

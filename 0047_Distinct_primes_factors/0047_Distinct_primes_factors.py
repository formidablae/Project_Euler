# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 * 7
# 15 = 3 * 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 * 7 * 23
# 645 = 3 * 5 * 43
# 646 = 2 * 17 * 19.

# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

import numpy as np
import primesieve


def check_has_prime_factors(n, distinct_count, primes):
    count = 0
    for prime in primes:
        if n % prime == 0:
            count += 1
        if count == distinct_count:
            return True
    return False

def count_total_with_prime_factors(n, distinct_count, primes):
    count = 0
    for i in range(distinct_count):
        if check_has_prime_factors(
            n + i,
            distinct_count,
            primes
        ):
            count += 1
        else:
            break
    return count

def main():
    it = primesieve.Iterator()
    number = 2
    # distinct_count = 2
    # distinct_count = 3
    distinct_count = 4
    
    primes = []
    for i in range(distinct_count):
        primes.append(it.next_prime())

    while True:
        if number > primes[-1]:
            primes.append(it.next_prime())

        if count_total_with_prime_factors(number, distinct_count, primes) == distinct_count:
            print(number)
            break
        
        number += 1
    
if __name__ == '__main__':
    main()

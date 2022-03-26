# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?


import primesieve


def get_primes_smaller_than(n):
    result = []
    it = primesieve.Iterator()
    prime = it.next_prime()
    while prime < n:
        result.append(prime)
        prime = it.next_prime()
    return result


def prime_witten_most_consecutive_prime_sum(primes, primes_set, ceiling):
    arg_max_sum_primes = 0
    max_length = -1
    for i in range(len(primes)):
        max_sum = 0
        for j in range(i, len(primes)):
            max_sum += primes[j]
            if max_sum > ceiling:
                break
            if max_sum in primes_set and max_sum > arg_max_sum_primes and j - i > max_length:
                max_length = j - i
                arg_max_sum_primes = max_sum
    return arg_max_sum_primes, max_length


def main():
    primes = get_primes_smaller_than(1000000)
    primes_set = set(primes)
    arg_max_sum_primes, max_length = prime_witten_most_consecutive_prime_sum(primes, primes_set, 1000000)
    print(
        "{} can be written as the sum of the most consecutive primes, with {} consecutive primes".format(
            arg_max_sum_primes, max_length
        )
    )


if __name__ == "__main__":
    main()

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2*1^2
# 15 = 7 + 2*2^2
# 21 = 3 + 2*3^2
# 25 = 7 + 2*3^2
# 27 = 19 + 2*2^2
# 33 = 31 + 2*1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


from math import ceil

from primesieve import primes


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(ceil(n**0.5)) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_list(n):
    return list(primes(n))


def is_written_as_prime_and_twice_a_square(n):
    primes = primes_list(n - 2)
    twice_squares = [2 * i * i for i in range(1, int(ceil((n / 2) ** 0.5) + 1))]
    for prime in primes:
        for two_square in twice_squares:
            if prime + two_square == n:
                print(n, "=", prime, "+ 2 *", int((two_square // 2) ** 0.5), "^2")
                return True
                return True
            elif prime + two_square > n:
                break
    return False


def main():
    num = 1
    while True:
        if is_prime(num):
            num += 2
            continue
        if not is_written_as_prime_and_twice_a_square(num):
            print(num, "is the smallest odd composite that cannot be written as the sum of a prime and twice a square")
            break
        num += 2


main()

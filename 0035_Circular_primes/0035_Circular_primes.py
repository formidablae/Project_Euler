# The number, 197, is called a circular prime because
# all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_circular_prime(n):
    if len(str(n)) == 1:
        return is_prime(n)
    digits = [int(x) for x in str(n)]
    for i in range(len(digits)):
        if not is_prime(int("".join(str(x) for x in digits[i:] + digits[:i]))):
            return False
    return True


def main():
    circular_primes = []
    for n in range(2, 1000000):
        if is_circular_prime(n):
            circular_primes.append(n)
    print("Circular primes:", circular_primes)
    print("Total circular primes:", len(circular_primes))


main()

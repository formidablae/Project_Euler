# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_truncatable_prime(n):
    if len(str(n)) == 1:
        return False
    digits = [int(x) for x in str(n)]
    for i in range(len(digits)):
        if len(digits[i:]) > 0 and not is_prime(int("".join(str(x) for x in digits[i:]))):
            return False
        if len(digits[:i]) > 0 and not is_prime(int("".join(str(x) for x in digits[:i]))):
            return False
    return True


def main():
    truncatable_primes = []
    n = 11
    while len(truncatable_primes) < 11:
        if n % 100000 < 2:
            print("done", n)
        if is_truncatable_prime(n):
            truncatable_primes.append(n)
        n += 2
    print("Truncatable primes:", truncatable_primes)
    print("Total truncatable primes:", len(truncatable_primes))
    print("Sum of truncatable primes:", sum(truncatable_primes))


main()

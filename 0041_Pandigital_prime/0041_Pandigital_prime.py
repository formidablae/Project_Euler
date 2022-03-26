# We shall say that an n-digit number is pandigital
# if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?


import primesieve


def is_pandigital(num):
    num_str = str(num)
    if len(set(num_str)) != len(num_str):
        return False
    for i in range(1, len(num_str) + 1):
        if str(i) not in num_str:
            return False
    return True


def main():
    it = primesieve.Iterator()
    prime = 2143
    largest_pandigital_prime = prime
    while len(str(prime)) < 9:
        if is_pandigital(prime):
            largest_pandigital_prime = prime
        prime = it.next_prime()
    print(largest_pandigital_prime)


main()

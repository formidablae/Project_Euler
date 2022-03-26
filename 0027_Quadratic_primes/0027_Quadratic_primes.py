# Euler discovered the remarkable quadratic formula:
#
# n² + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <=39.
# However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
#
# The incredible formula n² − 79n + 1601 was discovered,
# which produces 80 primes for the consecutive values 0 <= n <= 79.
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
# n² + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces
# the maximum number of primes for consecutive values of n, starting with n = 0.


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def quadratic_primes(a, b):
    n = 0
    while is_prime(n**2 + a * n + b):
        n += 1
    return n - 1


a = -999
b = -999
max_n = 0
a_for_max_n = -999
b_for_max_n = -999
while a <= 999:
    while b <= 999:
        n = quadratic_primes(a, b)
        if n > max_n:
            max_n = n
            a_for_max_n = a
            b_for_max_n = b
            print(a_for_max_n, b_for_max_n, max_n, n**2 + a * n + b)
        b += 1
    a += 1
    b = -999
print("max_n =", max_n)
print("a * b =", a_for_max_n * b_for_max_n)

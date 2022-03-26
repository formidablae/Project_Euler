# The fraction 49/98 is a curious fraction,
# as an inexperienced mathematician in attempting to simplify
# it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like,
# 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.


def is_digit_cancelling_fraction(n, d):
    if n / d >= 1:
        return False
    n_digits = [int(x) for x in str(n)]
    d_digits = [int(x) for x in str(d)]
    if n_digits[1] == 0 and d_digits[1] == 0:
        # trivial
        return False
    if n_digits[0] == d_digits[0] and d_digits[1] != 0 and n / d == n_digits[1] / d_digits[1]:
        return True
    if n_digits[0] == d_digits[1] and n / d == n_digits[1] / d_digits[0]:
        return True
    if n_digits[1] == d_digits[0] and d_digits[1] != 0 and n / d == n_digits[0] / d_digits[1]:
        return True
    if n_digits[1] == d_digits[1] and n / d == n_digits[0] / d_digits[0]:
        return True
    return False


def all_digit_cancelling_fractions():
    for n in range(10, 100):
        for d in range(n + 1, 100):
            if is_digit_cancelling_fraction(n, d):
                yield n, d


def simplify_fraction(n, d):
    for i in range(2, min(n, d) + 1):
        if n % i == 0 and d % i == 0:
            n = n // i
            d = d // i
            return simplify_fraction(n, d)
    return n, d


digit_cancelling_fractions = all_digit_cancelling_fractions()
product = (1, 1)
for frac in digit_cancelling_fractions:
    product = (product[0] * frac[0], product[1] * frac[1])
    print(frac)
print("Product of digit cancelling fractions:", product)
print("Simplified product:", simplify_fraction(product[0], product[1]))

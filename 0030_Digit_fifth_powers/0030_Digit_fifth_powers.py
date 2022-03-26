# Surprisingly there are only three numbers that can be written
# as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def pth_powers(n, p):
    """
    Returns the sum of the p-th powers of the digits of n.
    """
    return sum(map(lambda x: x**p, map(int, str(n))))


def max_pth_power_for_digits(d, p):
    """
    Returns the maximum pth powers of a d digits number.
    """
    return d * 9**p


def max_number_greater_than_pth_power_for_digits(p):
    """
    Returns the maximum number greater than the fourth power its length of digits.
    """
    not_passing = 0
    max_number = 2
    while not_passing < 10:
        length_of_digits = len(str(max_number))
        if max_pth_power_for_digits(length_of_digits, p) < max_number:
            not_passing += 1
        else:
            max_number *= 10
    return max_number


def sum_pth_powers(p):
    """
    Returns the sum of all numbers that can be written as the sum of pth powers of their digits.
    """
    x = 2
    res = 0
    max_number = max_number_greater_than_pth_power_for_digits(p)
    print("max_number =", max_number)
    while x <= max_number:
        if x == pth_powers(x, p):
            print("x =", x)
            res += x
        x += 1
    return res


print(sum_pth_powers(4))
print(sum_pth_powers(5))

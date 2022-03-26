# The square root of 2 can be written as an infinite continued fraction.
#
# √2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... )))
#
# The infinite continued fraction can be written,
# √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum.
# In a similar way, √23 = [4;(1,3,1,8)].
#
# It turns out that the sequence of partial values of continued
# fractions for square roots provide the best rational approximations.
# Let us consider the convergents for √2.
#
# 1 + 1/2 = 3/2
#
# 1 + 1/(2 + 1/2) = 7/5
#
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12
#
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29
#
# Hence the sequence of the first ten convergents for √2 are:
#
# 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
#
# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
#
# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
#
# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
#
# Find the sum of digits in the numerator of the
# 100th convergent of the continued fraction for e.

import math


def infinite_continued_fraction_for_two(nth) -> list:
    """
    Returns list of the first n (numerator, denominator)
    of the square root partial fractions of number 2.

    nth = 1, return [(1, 1)]
    nth = 2, return [(1, 1), (3, 2)]
    nth = 3, return [(1, 1), (3, 2), (7, 5)]
    nth = 4, return [(1, 1), (3, 2), (7, 5), (17, 12)]
    """
    res = [(1, 1), (3, 2), (7, 5)]
    for i in range(3, nth):
        n_i = res[i - 1][0] + 2 * res[i - 1][1]
        d_i = 2 * res[i - 1][1] + res[i - 2][1]
        res.append((n_i, d_i))
    return res


def infinite_continued_fraction_for_e(nth) -> list:
    """
    Returns list of the first n (numerator, denominator)
    of the square root partial fractions of number e.

    nth = 1, return [(2, 1)]
    nth = 2, return [(2, 1), (3, 2)]
    nth = 3, return [(2, 1), (3, 2), (8, 3)]
    nth = 4, return [(2, 1), (3, 2), (8, 3), (11, 4)]
    """
    res = [(2, 1), (3, 2), (8, 3), (11, 4)]
    for i in range(4, nth):
        if (i + 1) % 3 == 0:
            n_i = 2 * ((i + 1) // 3) * res[i - 1][0] + res[i - 2][0]
            d_i = 2 * ((i + 1) // 3) * res[i - 1][1] + res[i - 2][1]
        else:
            n_i = res[i - 1][0] + res[i - 2][0]
            d_i = res[i - 1][1] + res[i - 2][1]
        res.append((n_i, d_i))
    return res


def main():
    fractions_for_two = infinite_continued_fraction_for_two(10)
    fractions_for_e_ten = infinite_continued_fraction_for_e(10)
    fractions_for_e_hundred = infinite_continued_fraction_for_e(100)
    print(fractions_for_two)
    print(fractions_for_e_ten)
    print("The 100th convergent of the continued fraction for e:", fractions_for_e_hundred[99])
    print(
        "Sum of digits in numerator of the 100th convergent",
        "of the continued fraction for e:",
        sum(int(i) for i in str(fractions_for_e_hundred[99][0])),
    )


main()

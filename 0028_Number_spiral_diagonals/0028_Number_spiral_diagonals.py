# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def spiral_diagonals_iterative(n):
    """
    Returns the sum of the diagonals in a n by n spiral.
    """
    res = 0
    i = 1
    c = 1
    while i <= n**2:
        # print("i =", i)
        # print("c =", c)
        # print("res =", res)
        res += i
        i += 2 * c
        if i == (2 * c + 1) ** 2:
            c += 1
    return res


print(spiral_diagonals_iterative(1))
print(spiral_diagonals_iterative(2))
print(spiral_diagonals_iterative(3))
print(spiral_diagonals_iterative(4))
print(spiral_diagonals_iterative(5))
print(spiral_diagonals_iterative(1001))

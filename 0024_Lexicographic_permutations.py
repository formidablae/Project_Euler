# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Solution:
def permutations(numbers: list):
    """
    Generate all permutations of the given list of numbers.
    """
    if len(numbers) == 1:
        yield str(*numbers)
    else:
        for i, n in enumerate(numbers):
            for perm in permutations(numbers[:i] + numbers[i+1:]):
                yield str(n) + perm
                
print(list(permutations([0, 1, 2])))
print(list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[999999])

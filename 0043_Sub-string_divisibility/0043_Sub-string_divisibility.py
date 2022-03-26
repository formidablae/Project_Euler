# The number, 1406357289, is a 0 to 9 pandigital number
# because it is made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.

# Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:

# d_2d_3d_4 = 406 is divisible by 2
# d_3d_4d_5 = 063 is divisible by 3
# d_4d_5d_6 = 635 is divisible by 5
# d_5d_6d_7 = 357 is divisible by 7
# d_6d_7d_8 = 572 is divisible by 11
# d_7d_8d_9 = 728 is divisible by 13
# d_8d_9d_10 = 289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.


from itertools import permutations


def count_satisfied_divisions(number: str) -> int:
    primes: list = [2, 3, 5, 7, 11, 13, 17]
    count_divisibles: int = 0
    for i in range(1, 8):
        if int(number[i : i + 3]) % primes[i - 1] == 0:
            count_divisibles += 1

    return count_divisibles


def satisfy_divisibility_property(number: str) -> bool:
    return count_satisfied_divisions(number) == 7


def main():
    digits: str = "0123456789"
    pandigitals: list = list("".join(x) for x in permutations(digits))
    pandigitals_satisfy_property = list(filter(satisfy_divisibility_property, pandigitals))
    pandigitals_satisfy_property_int = list(map(int, pandigitals_satisfy_property))
    print(pandigitals_satisfy_property_int)
    print(sum(pandigitals_satisfy_property_int))


if __name__ == "__main__":
    main()

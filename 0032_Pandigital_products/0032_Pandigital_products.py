# We shall say that an n-digit number is pandigital
# if it makes use of all the digits 1 to n exactly once
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 * 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way
# so be sure to only include it once in your sum.

from itertools import permutations


def pandigital_products(l):
    import itertools
    digits = list(range(1, l + 1))
    expressions = set()
    products = set()
    for i in range(1, len(digits) // 2 + 1):
        index_perms_for_multiplicand = list(itertools.permutations(digits, i))
        for j in range(len(index_perms_for_multiplicand)):
            multiplicand = []
            left_numbers = []
            for k in range(len(index_perms_for_multiplicand[j])):
                multiplicand.append(index_perms_for_multiplicand[j][k])
            for dig in digits:
                if dig not in multiplicand:
                    left_numbers.append(dig)
            for m in range(1, len(digits) // 2 + 1):
                index_perms_for_multiplier = list(itertools.permutations(left_numbers, m))
                for n in range(len(index_perms_for_multiplier)):
                    multiplier = []
                    left_product = []
                    for o in range(len(index_perms_for_multiplier[n])):
                        multiplier.append(index_perms_for_multiplier[n][o])
                    for other_dig in left_numbers:
                        if other_dig not in multiplier:
                            left_product.append(other_dig)
                    product_perms = list(itertools.permutations(left_product, len(left_product)))
                    for prod in product_perms:
                        multiplicand_str_int = int(
                            ''.join(str(x) for x in multiplicand))
                        multiplier_str_int = int(
                            ''.join(str(y) for y in multiplier))
                        product_str_int = int(
                            ''.join(str(z) for z in prod))
                        if multiplicand_str_int > product_str_int:
                            continue
                        if multiplier_str_int > product_str_int:
                            continue
                        if multiplicand_str_int * multiplier_str_int != product_str_int:
                            continue
                        expression = str(multiplicand_str_int) + ' * ' + \
                            str(multiplier_str_int) + \
                            ' = ' + str(product_str_int)
                        expressions.add(expression)
                        print(expression)
                        if product_str_int in products:
                            continue
                        products.add(product_str_int)
    return products


print(sum(pandigital_products(9)))

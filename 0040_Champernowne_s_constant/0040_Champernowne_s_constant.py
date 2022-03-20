# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part,
# find the value of the following expression.

# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

def main():
    number_position = {}
    irrational_decimal_part = ""
    numb = 1
    while len(irrational_decimal_part) < 1000000:
        i = 0
        for c in str(numb):
            number_position[len(irrational_decimal_part) + 1] = int(c)
            irrational_decimal_part += c
            i += 1
        # print("numb =", numb, "number_position[", str(len(irrational_decimal_part)), "] =", 
        #       number_position[len(irrational_decimal_part)])
        numb += 1
    print(
        number_position[1] * \
        number_position[10] * \
        number_position[100] * \
        number_position[1000] * \
        number_position[10000] * \
        number_position[100000] * \
        number_position[1000000]
    )

main()

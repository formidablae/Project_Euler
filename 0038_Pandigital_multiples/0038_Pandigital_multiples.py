# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital,
# 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9
# and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number
# that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def is_pandigital(num):
    num_str = str(num)
    return len(num_str) == 9 and len(set(num_str)) == 9

def concatenated_product(m, n):
    result = ''
    for i in range(1, n+1):
        result += str(i * m)
    return int(result)

def main():
    max_nine_digit_pandigital = 0
    mm = 1
    while len(str(mm)) < 5:
        if mm % 10 == 0:
            mm += 1
            continue
        nn = 2
        while nn < 10:
            if nn % 10 == 0 or \
               len(str(mm * nn)) > 9 or \
               len(str(mm)) * nn > 9 or \
               (mm % 2 == 0 and (nn % 5 == 0 or nn > 5)):
                nn += 1
                continue
            concatenated = concatenated_product(mm, nn)
            if "0" in set(str(concatenated)):
                nn += 1
                continue
            if len(str(concatenated)) > 9:
                break
            if is_pandigital(concatenated):
                max_nine_digit_pandigital = max(max_nine_digit_pandigital, concatenated)
            nn += 1
            # print("mm =", mm, "nn =", nn,
            #       "max_nine_digit_pandigital =", max_nine_digit_pandigital)
        mm += 1
    print(max_nine_digit_pandigital)

main()

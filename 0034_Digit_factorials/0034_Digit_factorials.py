# 145 is a curious number,
# as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.


def is_curious_number(n, factorials):
    digits = [int(x) for x in str(n)]
    return n == sum(factorials[y] for y in digits)


def get_max_ceiling_number(factorials):
    digits = len(str(factorials[9]))
    while True:
        if int("9" * digits) > factorials[9] * digits:
            break
        digits += 1
    return int("9" * digits)


def main():
    curious_numbers = []
    factorials = {}
    factorials[0] = 1
    s = 1
    for i in range(1, 10):
        s *= i
        factorials[i] = s
    print("Factorials:", factorials)
    max_ceiling_number = get_max_ceiling_number(factorials)
    print("Max ceiling number:", max_ceiling_number)
    for n in range(10, max_ceiling_number):
        if is_curious_number(n, factorials):
            curious_numbers.append(n)
        if n % 1000000 == 0:
            print("Checked:", n)
    print("Total curious numbers:", len(curious_numbers))
    print("Curious numbers:", curious_numbers)
    print("Sum of curious numbers:", sum(curious_numbers))


main()

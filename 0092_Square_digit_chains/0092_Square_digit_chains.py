# A number chain is created by continuously adding the square of the digits
# in a number to form a new number until it has been seen before.

# For example,

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
# What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?


def arrives_at_89(n):
    if n == 0:
        return False
    while True:
        if n == 1:
            return False
        if n == 89:
            return True
        n = sum([int(i) ** 2 for i in str(n)])


def count_89_chains(m):
    count = 0
    for i in range(m):
        if arrives_at_89(i):
            count += 1
    return count


def main():
    print(count_89_chains(10000000))


main()

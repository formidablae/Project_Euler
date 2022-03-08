# A unit fraction contains 1 in the numerator.
# The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def periodic_cycle(n):
    """
    Find the length of the recurring cycle of 1/n.
    """
    remainder = 1
    remainders = []
    while remainder not in remainders:
        remainders.append(remainder)
        remainder = (remainder * 10) % n
    return len(remainders) - remainders.index(remainder)

print("number =", 3, "periodic cycle =", periodic_cycle(3))
print("number =", 6, "periodic cycle =", periodic_cycle(6))
print("number =", 7, "periodic cycle =", periodic_cycle(7))
print("number =", 9, "periodic cycle =", periodic_cycle(9))

max_peiodic_cycle = 0
number = 1
for d in range(1, 1000):
    if periodic_cycle(d) > max_peiodic_cycle:
        max_peiodic_cycle = periodic_cycle(d)
        number = d
print("number =", number, "periodic cycle =", max_peiodic_cycle)

# A positive fraction whose numerator is less than its denominator is called a proper fraction.
# For any denominator, d, there will be d-1 proper fractions
# for example, with d = 12:
# 1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12.

# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient
# for example, R(12) = 4/11 .
# In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

# Find the smallest denominator d, having a resilience R(d) < 15499/94744 .


from primesieve import primes


def main():
    target = 15499 / 94744
    min_resilience = 1
    primes_arr = primes(30)
    n = 1
    d = 1
    count = 1
    for i in range(len(primes_arr)):
        n *= primes_arr[i] - 1
        d *= primes_arr[i]
        for j in range(2, primes_arr[i]):
            num = n * j
            den = d * j
            resilience = num / (den - 1)
            min_resilience = min(resilience, min_resilience)
            if resilience < target:
                print("\nnumber:", den)
                print("final resilience:", resilience)
                print("target:", target)
                exit(0)
            if count % 10 == 0:
                print("\nDone:", count)
                print("min resilience obtained:", min_resilience)
            count += 1


main()

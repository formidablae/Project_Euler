# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways:
# (i) each of the three terms are prime, and ,
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?


import primesieve
from itertools import permutations


def prime_permutations(primes_list, min_digits, max_digits):
    primes_set = set(primes_list)
    prime_perms = {}
    for prime in primes_list:
        perms_int = sorted(
            list(
                set(
                    [
                        int("".join(x))
                        for x in permutations(str(prime))
                        if int("".join(x)) in primes_set
                    ]
                )
            )
        )
        if len(perms_int) <= 2:
            continue
        prime_perms[prime] = perms_int
    return prime_perms


def equidistant_prime_perms(prime_perms):
    results = set()
    for prime, perms in prime_perms.items():
        for i in range(len(perms)):
            for j in range(i + 1, len(perms)):
                for k in range(j + 1, len(perms)):
                    if perms[j] - perms[i] == perms[k] - perms[j]:
                        results.add(str(perms[i]) + str(perms[j]) + str(perms[k]))
    return results


def main():
    primes = list(primesieve.primes(10000))
    primes_list = list(filter(lambda x: x > 1000, primes))

    prime_perms = prime_permutations(primes_list, 3, 4)
    results = equidistant_prime_perms(prime_perms)

    print(*results, sep="\n")


if __name__ == "__main__":
    main()

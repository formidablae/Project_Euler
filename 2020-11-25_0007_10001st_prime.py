def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


primes = [2]
i = 3
while len(primes) < 10001:
    if isPrime(i):
        primes.append(i)
    i += 1
print(primes[-1])
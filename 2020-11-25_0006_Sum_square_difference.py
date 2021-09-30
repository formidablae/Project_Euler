def sumofsquares(n):
    ans = 0
    for i in range(1, n + 1):
        ans += i ** 2
    return ans


def squareofsum(n):
    return sum(list(range(1, n + 1))) ** 2


print(abs(sumofsquares(10) - squareofsum(10)))
print(abs(sumofsquares(100) - squareofsum(100)))
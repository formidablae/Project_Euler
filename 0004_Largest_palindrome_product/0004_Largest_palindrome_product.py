def palindromicstring(numstr):
    return list(reversed(numstr)) == list(numstr)


def palindromicdecimal(n):
    return palindromicstring(str(n))


largestfound = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        if palindromicdecimal(i * j):
            if i * j > largestfound:
                largestfound = i * j
print(largestfound)

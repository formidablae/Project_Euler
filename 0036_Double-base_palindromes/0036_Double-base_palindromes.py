def palindromicstring(numstr):
    return list(reversed(numstr)) == list(numstr)


def palindromicdecimal(n):
    return palindromicstring(str(n))


def palindromicbinary(n):
    return palindromicstring(str(bin(n))[2:])


number = 1
summation = 0
while number < 1000000:
    if palindromicdecimal(number) and palindromicbinary(number):
        summation += number
        print("number decimal = {}, number binary = {}, sum = {}".format(number, str(bin(number))[2:], summation))
    number += 2

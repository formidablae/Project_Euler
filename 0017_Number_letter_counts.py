def convert(num):
    units = ("", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
             "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens = ("", "", "twenty ", "thirty ", "forty ", "fifty ",
            "sixty ", "seventy ", "eighty ", "ninety ")

    if num < 0:
        return "minus "+convert(-num)
    
    if num < 20:
        return units[num]

    if num < 100:
        return tens[num // 10] + units[int(num % 10)]

    if num < 1000 and num % 100 == 0:
        return units[num // 100] + "hundred "
    
    if num < 1000:
        return units[num // 100] + "hundred and " + convert(int(num % 100))

    if num < 1000000 and num % 1000 == 0:
        return convert(num // 1000) + "thousand "

    if num < 1000000:
        return convert(num // 1000) + "thousand and " + convert(int(num % 1000))

    if num < 1000000000 and num % 1000000 == 0:
        return convert(num // 1000000) + "million "
    
    if num < 1000000000:
        return convert(num // 1000000) + "million and " + convert(int(num % 1000000))

    return convert(num // 1000000000) + "billion and " + convert(int(num % 1000000000))

count_letters = 0
for i in range(1, 1001):
    count_letters += len(convert(i).replace(" ", ""))
print(count_letters)

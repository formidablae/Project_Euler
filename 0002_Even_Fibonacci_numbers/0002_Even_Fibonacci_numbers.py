number1 = 1
number2 = 2
summation = 0
while number2 < 4000000:
    summation += number2
    number1, number2 = number2, number1 + number2
    number1, number2 = number2, number1 + number2
    number1, number2 = number2, number1 + number2
print(summation)

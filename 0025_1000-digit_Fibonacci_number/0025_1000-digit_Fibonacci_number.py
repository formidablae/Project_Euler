number1 = 1
number2 = 1
index = 2
while len(str(number2)) < 1000:
    number1, number2 = number2, number1 + number2
    index += 1
    print("len = {}, index = {}".format(len(str(number2)), index))

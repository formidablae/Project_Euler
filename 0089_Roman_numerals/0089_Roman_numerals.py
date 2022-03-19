# For a number written in Roman numerals to be considered valid
# there are basic rules which must be followed.
# Even though the rules allow some numbers to be expressed in more than one way
# there is always a "best" way of writing a particular number.

# For example, it would appear that there are at least six ways of writing the number sixteen:

# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI

# However, according to the rules only XIIIIII and XVI are valid,
# and the last example is considered to be the most efficient,
# as it uses the least number of numerals.

# The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
# contains one thousand numbers written in valid,
# but not necessarily minimal, Roman numerals
# see About... Roman Numerals for the definitive rules for this problem.

# Find the number of characters saved by writing each of these in their minimal form.

# Note: You can assume that all the Roman numerals in the file
# contain no more than four consecutive identical units.

def read_roman_numerals(filename):
    numerals = []
    with open(filename) as f:
        for line in f:
            numerals.append(line.strip())
    return numerals


def roman_numeral_to_int(numeral):
    # convert roman numeral to integer
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    for i in range(0, len(numeral)):
        if i > 0 and values[numeral[i]] > values[numeral[i - 1]]:
            result += values[numeral[i]] - 2 * values[numeral[i - 1]]
        else:
            result += values[numeral[i]]
    return result


def int_to_roman_numeral(integer):
    # convert integer to roman numeral, efficiently
    values = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
              100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
              10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result = ''
    for i in sorted(values.keys(), reverse=True):
        while integer >= i:
            result += values[i]
            integer -= i
    return result
    

def main():
    roman_numerals = read_roman_numerals('p089_roman.txt')
    saved_chars = 0
    for roman_numeral in roman_numerals:
        saved_chars += len(roman_numeral) - len(int_to_roman_numeral(roman_numeral_to_int(roman_numeral)))
    print(saved_chars)

main()

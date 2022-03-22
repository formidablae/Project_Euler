# The nth term of the sequence of triangle numbers is given by,
# t_n = (1/2) * n * (n+1) so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then
# we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?

import numpy as np


def read_words(filename):
    return np.genfromtxt(filename, dtype='str', delimiter=',')


def is_triangle_number(t_n):
    # n^2 + n - 2 * t_n = 0
    n = (-1 + np.sqrt(1 + 8 * t_n)) / 2
    try:
        return n == int(n)
    except ValueError:
        return False


def word_value(word):
    word_value = sum([ord(letter) - ord('A') + 1 for letter in word])
    # print("word {} has {} value".format(word, word_value))
    return word_value


def is_triangle_word(word):
    is_triangle_word = is_triangle_number(word_value(word))
    # print("Is {} a triangle word? {}".format(word, is_triangle_word))
    return is_triangle_word


def main():
    words = read_words('p042_words.txt')
    stripped_words = [word.strip('"') for word in words]
    print("{} words are triangle words".format(sum([1 for word in stripped_words if is_triangle_word(word)])))
    

if __name__ == '__main__':
    main()

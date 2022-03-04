# Using names.txt(right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?


def read_sorted_names(filename):
    with open(filename) as f:
        names = f.read().replace('"', "").split(',')
    return sorted(names)

def name_scores(names):
    result = {}
    for ind, name in enumerate(names):
    # print(result)
        sum_letters = 0
        for letter in name:
            sum_letters += ord(letter) - 64
        result[name] = sum_letters * (ind + 1)
    return result

sorted_names = read_sorted_names('p022_names.txt')
scores = name_scores(sorted_names)
# print(scores)
# print(name_scores(['COLIN']))
print("COLIN score:", scores.get('COLIN'))
print("Total:", sum(scores.values()))

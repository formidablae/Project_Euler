# A common security method used for online banking is
# to ask the user for three random characters from a passcode.
# For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters
# the expected reply would be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order,
# analyse the file so as to determine the shortest possible secret passcode of unknown length.


################################################
# TOO MUCH MEMORY FOR LONG KEY. TODO: OPTIMIZE #
################################################


from itertools import combinations, product

import numpy as np


def read_keylog(filename):
    return np.loadtxt(filename, dtype=str, delimiter='\n')


def get_digits(n):
    return [int(i) for i in str(n)]


def main():
    keys_inserted_str = read_keylog("p079_keylog.txt")
    # keys_inserted_str = ["317"]
    
    length = 5
    digits_str = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    digits_int = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        print("Searching for possible full keys with length:", length)
            
        possible_indices_str_arr = list(combinations(digits_int[:length], 3))

        possible_full_keys_set = set("".join(key_list) for key_list in product(digits_str, repeat=length))
        found_at_least_one_before = False
        for key_inserted in keys_inserted_str:
            print("Checking inserted key", key_inserted, ". Length of found possible full keys:", len(possible_full_keys_set))
            possible_full_keys_for_this_inserted_key = set()
            found_at_least_one_before_for_this_inserted_key = False

            for possible_full_key in possible_full_keys_set:
                for possible_index in possible_indices_str_arr:

                    if possible_full_key[possible_index[0]] + \
                        possible_full_key[possible_index[1]] + \
                            possible_full_key[possible_index[2]] == key_inserted:
                        possible_full_keys_for_this_inserted_key.add(possible_full_key)
                        found_at_least_one_before_for_this_inserted_key = True

            if found_at_least_one_before and len(possible_full_keys_set) == 0:
                break
            if found_at_least_one_before:
                # intersect sets possible_full_keys_set and possible_full_keys_for_this_inserted_key
                possible_full_keys_set = possible_full_keys_set.intersection(
                    possible_full_keys_for_this_inserted_key
                )
            else:
                possible_full_keys_set = possible_full_keys_for_this_inserted_key
                found_at_least_one_before = found_at_least_one_before_for_this_inserted_key

        if found_at_least_one_before and len(possible_full_keys_set) == 0:
            # full key with that length not possible, increase length
            print("Full key with that length", length, "not possible, increase length to", length + 1)
            length += 1
        else:
            # found something
            print("\nFound something. List of all possible full keys:", sorted(list(possible_full_keys_set)))
            break
    
main()

collatz_sequences = {}
collatz_sequences[1] = 1


def len_of_collatz_sequence(n):
    count = 1
    if n in collatz_sequences.keys():
        return collatz_sequences[n]
    if n % 2 == 0:
        count = 1 + len_of_collatz_sequence(n // 2)
    else:
        count = 1 + len_of_collatz_sequence(3 * n + 1)
    collatz_sequences[n] = count
    return count


max_chain_length = 0
for i in range(1, 1000000):
    max_chain_length = max(max_chain_length, len_of_collatz_sequence(i))
for k in collatz_sequences.keys():
    if collatz_sequences[k] == max_chain_length:
        print(k)
        break

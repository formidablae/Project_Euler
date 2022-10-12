# Find the smallest x + y + z with integers x > y > z > 0
# such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.


def is_square(x):
    return x == int(x**0.5) ** 2


def solve():
    solution = {}
    i = 4
    while not solution:
        a = i**2

        for j in range(3, i):
            c = j**2
            f = a - c
            if not is_square(f):
                continue

            k_initial = 2 if j % 2 == 0 else 1

            for k in range(k_initial, j, 2):
                d = k**2
                e = a - d
                b = c - e

                if b <= 0 or not is_square(e) or not is_square(b):
                    continue

                x = int((a + b) / 2)
                y = int((e + f) / 2)
                z = int((c - d) / 2)

                solution = {"x": x, "y": y, "z": z, "x + y + z": x + y + z}
                break

        if solution:
            break
        i = i + 1

    return solution


print("\n".join([f"{k} = {v}" for k, v in solve().items()]))

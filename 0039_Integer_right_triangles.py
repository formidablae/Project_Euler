# If p is the perimeter of a right angle triangle with integral length sides,
# {a, b, c}, there are exactly three solutions for p = 120.

# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}

# For which value of p ≤ 1000, is the number of solutions maximised?

def perimeter(b, h):
    return b + h + (b ** 2 + h ** 2) ** 0.5

def main():
    count_sol = {}
    max_sol = 0
    a = 1
    while a <= 998:
        b = 1
        per = perimeter(a, b)
        while b <= 998 and per <= 1000:
            if a + b > 999:
                continue
            if per.is_integer():
                per = int(per)
                count_sol[per] = count_sol.get(per, 0) + 1
                if count_sol[per] > max_sol:
                    max_sol = count_sol[per]
            b += 1
            per = perimeter(a, b)
        a += 1
    print("perimeter, max solutions =", list(filter(lambda x: x[1] == max_sol, count_sol.items()))[0])
main()

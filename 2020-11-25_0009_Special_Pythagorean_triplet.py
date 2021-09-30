found = False
for a in range(1, 334):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        if 1000 * c + a * b == 500000:
            found = True
            break
    if found: break
print("a = {}, b = {}, c = {},\n"
      "a2 + b2 = c2: {} + {} = {},\n"
      "a + b + c = {},\n"
      "abc = {}".format(a, b, c, a ** 2, b ** 2, c ** 2, a + b + c, a*b*c))
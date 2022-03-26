sum = 0
for i in range(2, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
print(sum)

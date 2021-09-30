def process(n):
	print("Running. n = {}".format(n))
	s = ""
	while n > 1:
		if n % 3 == 0:
			n //= 3
			s += "D"
		elif n % 3 == 1:
			n = (4*n+2)//3
 			s += "U"
		else:
			n = (2*n-1)//3
			s += "d"
	return s

s = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
n = 2
i = 1
d = 1

while process(n)[:30] != s[:30]:
	while True:
		if process(n)[:i] == s[:i]:
			n1 = n
			break
		n += d
	n += d
	while True:
		if process(n)[:i] == s[:i]:
			n2 = n
			break
		n += d
	d = n2 - n1
	i += 1

while n < 10 ** 15:
	n += d

print("Complete n = {}, sequnce = {}".format(n, process(n)))

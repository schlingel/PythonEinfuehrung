x = 1
y = 1

print "Die ersten 10 Fibonacci-Zahlen sind:"

for i in range(10):
	print x,
	z = x
	x = y
	y = z + x


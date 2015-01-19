def fibonacci(n, x = 1, y = 1):
	if n > 0:
		print x
		fibonacci(n-1, y, x+y)

fibonacci(10)


x = -1
try:
	while int(x) < 0:
		x = raw_input("Geben Sie eine positive Zahl ein: ")
	print x + " ist positiv"
except ValueError:
	print "Das war keine Zahl, du Schlawiner!"


import sys


def elementary(x, y):
	print("Sum:\t\t", x + y)
	print("Difference:\t", x - y)
	print("Product:\t", x * y)
	if y == 0:
		print("Quotient:\t ERROR (div by zero)")
		print("Remainder:\t ERROR (modulo by zero)")
	else:
		print("Quotient:\t", x / y)
		print("Remainder:\t", x % y)


def print_error():
	print("Usage: python operations.py")
	print("Example:\n    python operations.py 10 3")


if len(sys.argv) < 3:
	print_error()
elif len(sys.argv) > 3:
	print("Input Error: too many arguments")
	print_error()
elif not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
	print("Input Error: only numbers\n")
	print_error()
else:
	x = int(sys.argv[1])
	y = int(sys.argv[2])
	elementary(x, y)

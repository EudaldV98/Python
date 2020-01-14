import sys


if len(sys.argv) != 3 or sys.argv[1].isdigit() or not sys.argv[2].isdigit():
	print('ERROR')
	sys.exit(0)

words = list(sys.argv[1].split(" "))
for i in words:
	if len(i) <= int(sys.argv[2]):
		words.remove(i)
print(words)
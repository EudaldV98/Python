import sys
import random


def generator(text, sep = ' ', option = None):
	"""Option is an optional arg, sep mandatory"""
	lst = text.split(sep)
	if option == 'shuffle':
		random.shuffle(lst)
	elif option == 'unique':
		lst = set(lst)
		lst = (list(lst))
	elif option == 'ordered':
		lst.sort()
	for i in lst:
		yield i

for t in generator(sys.argv[1], ' ', 'ordered'):
	print(t)
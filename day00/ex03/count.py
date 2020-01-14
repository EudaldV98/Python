import sys
import string


def text_analyzer(s = ""):
	if not s:
		print("What is the text to analyse?")
		s = input()
	print('- ' + str(sum(1 for c in s if c.isupper())) + " upper letters")
	print('- ' + str(sum(1 for c in s if c.islower())) + " lower letters")
	print('- ' + str(sum(1 for c in s if c in string.punctuation)) + " punctuation marks")
	print('- ' + str(sum(1 for c in s if c.isspace())) + " spaces")

sandwich = {
	'ingredients' : ['ham', 'bread', 'tomatoes'],
	'meal' : 'lunch',
	'prep_time' : 10
}

cake = {
	'ingredients' : ['flour', 'sugar', 'eggs'],
	'meal' : 'dessert',
	"prep_time" : 60
}

salad = {
	'ingredients' : ['avocado', 'argula', 'tomatoes'],
	'meal' : 'lunch',
	'prep_time' : 15
}

cookbook = {
	'sandwich' : sandwich,
	'cake' : cake,
	'salad' : salad
}

def	print_receipe(s):
	if s in cookbook.keys():
		print("I'm here")
	else:
		print("Nope")

s = input()
print_receipe(s)

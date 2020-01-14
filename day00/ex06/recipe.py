import sys


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

def	print_recipe(s):
	if s in cookbook.keys():
		print('Ingredient list: %s' % format(cookbook[s]['ingredients']))
		print('To be eaten for %s.' % format(cookbook[s]['meal']))
		print('Takes %s minutes of cooking.' % format(cookbook[s]['prep_time']))
	else:
		print("This recipe does not exist in the cookbook yet.")

def delete_recipe(s):
	if s in cookbook:
		cookbook.pop(s)
		print('%s was successfully removed from the cookbook.' % format(s))
	else:
		print('%s is not in the cookbook.' % format(s))

def add_recipe(n, i, m, t):
	if n not in cookbook:
		cookbook[n] = {}
		cookbook[n].update({'ingredients' : i})
		cookbook[n].update({'meal' : m})
		cookbook[n].update({'prep_time' : t})
	else:
		print('Nope')
	
exit = 0
while exit == 0:
	print('Please select an option by typing the corresponding number:')
	print('1: Add a recipe')
	print('2: Delete a recipe')
	print('3: Print a recipe')
	print('4: Print the cookbook')
	print('5: Quit')
	s = input()
	if s == '1':
		print('\nWhich is the name of the recipe?.')
		n = input()
		print('What are the ingredients needed?')
		i = input()
		print('Which type of meal is it?')
		m = input()
		print('What is the time of preparation?')
		t = input()
		add_recipe(n, i, m, t)	
	elif s == '2':
		print('\nWhich recipe do you want to delete?')
		s = input()
		delete_recipe(s)
	elif s == '3':
		print("\nPlease enter the recipe's name to get its details:")
		s = input()
		print('\n')
		print_recipe(s)
	elif s == '4':
		print('\nRecipes:')
		for i in cookbook:
			print(i)
	elif s == '5':
		print('\nCookbook closed')
		exit = 1
	else:
		print('\nThis option does not exist, please type the corresponding number.')
		print('To exit, enter 5.')
	if exit == 0:
		print('\n')

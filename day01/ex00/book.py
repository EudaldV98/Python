from recipe import Recipe
import datetime

class Book:
	def __init__(self, n, l_u, c_d, r_l):
		self.name = n
		self.last_update = l_u
		self.creation_date = c_d
		self.recipes_list = r_l
	
	def get_recipe_by_name(self, name):
		for obj in self.recipes_list['starter']:
			if obj.name == name:
				print(obj)
		for obj in self.recipes_list['lunch']:
			if obj.name == name:
				print(obj)
		for obj in self.recipes_list['dessert']:
			if obj.name == name:
				print(obj)
		pass

	def get_recipes_by_type(self, recipe_type):
		print('Recipes of type %s:' % format(recipe_type))
		for i in self.recipes_list[recipe_type]:
			print('-' , i.name)
		pass

	def add_recipe(self, recipe):
		if recipe not in Recipe.all_recipes:
			return
		elif recipe.recipe_type == 'starter':
			self.recipes_list['starter'].append(recipe)
		elif recipe.recipe_type == 'lunch':
			self.recipes_list['lunch'].append(recipe)
		elif recipe.recipe_type == 'dessert':
			self.recipes_list['dessert'].append(recipe)
		if not self.creation_date:
			self.creation_date = datetime.datetime.now()
			self.last_update = self.creation_date
		else:
			self.last_update = datetime.datetime.now()

class Recipe():
	all_recipes = []

	def __init__(self, n, c_l, c_t, i, d, r_t):
		self.name = n
		self.cooking_lvl = c_l
		self.cooking_time = c_t
		self.ingredients = i
		self.description = d
		self.recipe_type = r_t
		Recipe.all_recipes.append(self)


	def __str__(self):
		txt = ""
		txt += 'Name: %s.\n' % format(self.name)
		txt += 'Cooking lvl: %s.\n' % format(self.cooking_lvl)
		txt += 'Cooking Time: %s minutes.\n' % format(self.cooking_time)
		txt += 'Ingredients: %s\n' % format(self.ingredients)
		txt += 'Description: %s.\n' % format(self.description)
		txt += 'Meal type: %s.' % format(self.recipe_type)
		return txt
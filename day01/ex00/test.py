from book import Book
from recipe import Recipe
import datetime


salad = Recipe("salad", 1, 10, ["tomatoes", "lettuce", "mozza"], "simple salad", "starter")
sandwich = Recipe("sandwich", 1, 5, ["bread", "ham", "tomatoes", "olive oil"], "easy sandwich", "lunch")
melon = Recipe("melon with jam", 2, 10, ["melon", "ham (jamon)"], "typical slices of melon with ham", "starter")

#to_print = str(salad)
#print(to_print)

recipes_list = {
	'starter' : [],
	'lunch' : [],
	'dessert' : [],
}

cookbook = Book("cookbook", datetime.datetime.now(), datetime.date.today(), recipes_list)
cookbook.add_recipe(salad)
cookbook.add_recipe(melon)
cookbook.add_recipe(sandwich)
x = 1
cookbook.add_recipe(x)
cookbook.get_recipe_by_name('melon with jam')
#cookbook.get_recipes_by_type('starter')
print(cookbook.last_update)

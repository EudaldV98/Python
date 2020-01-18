import time
from random import randint
import sys


def log(func):
	def wrapper(*args, **kwargs):
		start_time = time.time()
		ret = func(*args, **kwargs)
		old_stdout = sys.stdout
		log_file = open('machine.log', 'a')
		sys.stdout = log_file
		print ("(jvaquer)Running: %s		" % func.__name__, "[exec-time = {:.3f}]".format((time.time() - start_time) * 1000))
		sys.stdout = old_stdout
		return ret
	return wrapper

class CoffeeMachine():

	water_level = 100
	
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print('Please add water!')
			return False
	
	@log
	def boil_water(self):
		return ('boiling...')

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print('Coffee is ready!')

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print('Blub blub blub...')

if __name__ == '__main__':

	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	
	machine.make_coffee()
	machine.add_water(70)
import numpy


class NumpyCreator():

	def __init__(self):
		self.arr = None

	def from_list(self, lst):
		if isinstance(lst, list):
			self.arr = numpy.array(lst)
		pass
	
	def from_tuple(self, tpl):
		if isinstance(tpl, tuple):
			self.arr = numpy.array(tpl)
		pass

	def from_iterable(self, itr):
		if hasattr(itr, '__iter__'):
			self.arr = numpy.array(itr)
		pass

	def from_shape(self, value):
		self.arr = numpy.zeros(value)
		pass

npc = NumpyCreator()
a = [2, 3, 4]
npc.from_list(a)
print(npc.arr)
b = ("a", "b", "c")
npc.from_tuple(b)
print(npc.arr)
z = (3,5)
npc.from_shape(z)
print(npc.arr)

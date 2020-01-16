import operator


class Vector:
	def __init__(self, lst):
		self.values = lst

	@classmethod
	def from_size(self, val):
		self.values = []
		for i in range(val):
			self.values.append(float(i))
		return self(self.values)
	
	@classmethod
	def from_range(self, rang):
		self.values = []
		i = rang[0]
		while (i < rang[1]):
			self.values.append(float(i))
			i += 1
		return self(self.values)

	def __add__(self, v):
		if isinstance(v, Vector) and len(self.values) == len(v.values):
				self.values = [x + y for x, y in zip(self.values, v.values)]
		else:
			self.values = [x + float(v) for x in self.values]
	
	def __radd__(self, nb):
		self.__add__(nb)
	
	def __sub__(self, v):
		if isinstance(v, Vector) and len(self.values) == len(v.values):
			self.values = [x - y for x, y in zip(self.values, v.values)]
		else:
			self.values = [x - float(v) for x in self.values]
	
	def __rsub__(self, nb):
		self.__sub__(nb)
	
	def __truediv__(self, v):
		new_value = []
		if isinstance(v, Vector) and len(self.values) == len(v.values):
			for x, y in zip(self.values, v.values):
				try:
					new_value.append(x / y)
				except ZeroDivisionError:
					new_value.append(x)
		else:
			for x in self.values:
				try:
					new_value.append(x / v)
				except ZeroDivisionError:
					new_value.append(x)
		self.values = new_value

	def __rtruediv__(self, nb):
		self.__truediv__(nb)
	
	def __mul__(self, v):
		if isinstance(v, Vector) and len(self.values) == len(v.values):
			self.values = [x * y for x, y in zip(self.values, v.values)]
		else:
			self.values = [x * float(v) for x in self.values]
	
	def __rmul__(self, nb):
		self.__mul__(nb)
	
	def __str__(self):
		text = ''
		text += str(self.values)
		return text
	
	def __repr__(self):
		return "%s(%r)" % (self.__class__, self.__dict__)
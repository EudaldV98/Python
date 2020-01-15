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

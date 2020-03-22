import sys
import pandas

class	FileLoader:
	
	def	__init__(self):
		pass
	
	@staticmethod
	def	load(path):
		try:
			data = pandas.read_csv(path)
		except:
			raise Exception(f"The file {path} does not exist.")
		print(f"Loading dataset of dimensions {data.shape[0]} x {data.shape[1]}.")
		return(data)

	@staticmethod
	def	display(df, n):
		if	n > 0:
			print(df.head(n))
		else:
			print(df.tail(abs(n)))

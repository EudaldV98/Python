import numpy
from PIL import Image


class ImageProcessor():

	def __init__(self):
		pass
	
	def load(self, path):
		try:
			img = Image.open(path)
			print(img)
		except IOError:
			pass

	def display(self, array):
		pass

im = ImageProcessor()
im.load("../assets/blue.png")


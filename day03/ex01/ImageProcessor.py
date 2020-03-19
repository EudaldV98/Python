import numpy
import scipy.misc
from PIL import Image


class ImageProcessor():

	def __init__(self):
		pass
	
	def load(self, path):
		try:
			img = Image.open(path)
			arr = numpy.array(img)
			return arr
		except IOError:
			pass

	def display(self, array):
		try:
			im = Image.fromarray(array)
			im.save("test.png")
			im.show("test.png")
		except IOError:
			pass


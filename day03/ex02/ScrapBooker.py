import numpy as np
from PIL import Image
import cv2

class ScrapBooker:
	
	def __init__(self):
		pass

	@staticmethod
	def crop(array, dimensions, position=(0,0)):
		if not isinstance(position,tuple):
			raise ValueError("The third argument must be a tuple (width,height)")
		if not isinstance(dimensions,tuple):
			raise ValueError("The second argument must be a tuple (width,height)")
		return array[position[0]:position[0]+dimensions[0],
					position[1]:position[1]+dimensions[1]]


	@staticmethod
	def	thin(array, n, axis):
		array = np.array(array)
		np.delete(array, n, axis=axis)
		return array

	@staticmethod
	def	juxtapose(array, n, axis):
		for i in range(n-1):
			array = np.concatenate((array, array), axis=0)
		return array



from ScrapBooker import ScrapBooker
import sys
sys.path.append('../ex01')

from ImageProcessor import ImageProcessor

try:
	img = ImageProcessor()
	arr = img.load('../assets/blue.png')
	newImage = ScrapBooker.crop(arr, (300,300))
	#newImage = ScrapBooker.thin(arr, 10, 1)
	#newImage = ScrapBooker.juxtapose(arr, 3, 0)
	img.display(newImage)

except ValueError as err:
	print(err)
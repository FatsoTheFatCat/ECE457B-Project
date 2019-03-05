from Pixel import Pixel

# The Image class is essentially a 2D array (or list of lists) of pixels
# Note that by this logic, a cluster of pixels is also effectively an image
# Also note that an image can be interpreted as composed of smaller images

# Class Members:
#		rows - The number of rows of pixels in the Image.
#				 - The size of the Image is given by rows x cols.
#				 - Note that the size is not meant to be changed after the Image is initialized.
#		cols - The number of columns of pixels in the Image. 
#				 - The size of the Image is given by rows x cols.
#				 - Note that the size is not meant to be changed after the Image is initialized.
#		pixels - The 2D array of pixels which make up the Image.

# Methods:
#		getRows - Returns the number of rows of pixels in the Image.
#		getColumns - Returns the number of columns of pixels in the Image.
#		getAllPixels - Returns the list of lists of pixels.
#	->setAllPixels - ? Not quite sure if this method should be a thing or if it should be initiated in __init__
#								 - Assigns the given (not sure what format yet) pixels to list of lists class member pixels.
#		getPixel - Returns the pixel at (x,y) of the Image if the location exists within the size of the Image.
#	->compareTo - Takes another Image as a parameter and returns whether the other Image is similar to this Image.
#							- Note that it compares for similarity, not an exact match. 
#							- Some level of fuzzy logic or neural network will likely be used here

class Image:
	rows = 0;
	cols = 0;
	pixels = None; # TO DO: determine if this is a thing in Python. The idea is to explicitly initiate pixels as Null but does this set it to None or to a NoneType?

	def __init__(self, rows, cols):
		self.rows = rows;
		self.cols = cols;
		self.pixels = [[Pixel(i,j) for j in range(cols)] for i in range(rows)];

	def getRows():
		return self.rows;

	def getColumns():
		return self.cols;

	def getAllPixels():
		return self.pixels;

	def setAllPixels(self, p):
		self.pixels = p;

	def getPixel(self, x, y):
		if (x < 0 || x >= rows || y < 0 || y >= cols):
			return None;

		return self.pixels[x][y];

	def compareTo(self, otherImg):
		# Placeholder comparison - this return statement will fail unless you pass itself as the otherImg too
		return (self == otherImg);


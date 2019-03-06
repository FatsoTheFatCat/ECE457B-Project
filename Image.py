from Pixel import Pixel

# The Image class is essentially a 2D array (or list of lists) of pixels.
# Note that by this logic, a cluster of pixels is also effectively an image.
# Also note that an image can be interpreted as composed of smaller images.

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
#							- Some level of fuzzy logic or neural network will likely be used here.
#		enhance - Enhances the quality of the Image by applying a Gaussian filter to reduce noise.
#						- Returns a new Image with the Gaussian filter applied to this Image.
# 	findGradient - Finds the image gradient.
#								 - Returns a new Image of the gradient.
#		applyThreshold - Applies a threshold filter on the Image given a threshold value as the parameter.
#									 - Returns a new binary Image with the threshold applied to this Image.
#		suppress - Suppressing non-maxima pixels in the Image.
#						 - Returns a new Image with the suppression applied to this Image.
#		linkEdgeSeg - Forms edges by linking edge segments given another binary Image with more noise.
#								- Returns a new Image with the edge segments linked. 
#		findEdges - Calls the necessary helper functions to find the edges in the Image.
#							- Returns a new Image with the edges identified. 

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
		if (x < 0 or x >= self.rows or y < 0 or y >= self.cols):
			return None;

		return self.pixels[x][y];



	def compareTo(self, otherImg):
		# Placeholder comparison - this return statement will fail unless you pass itself as the otherImg too
		return (self == otherImg);

	# TO DO: Decide whether the following functions should return a new Image or if the functions should be applied to this function
	def enhance(self):
		# Placeholder enhancement - apply Gaussian filter to reduce noise
		return self;

	def findGradient(self):
		# Placeholder for finding image gradient
		return self;

	def applyThreshold(self, threshold):
		# Placeholder for threshold
		return self;

	def suppress(self):
		# Placeholder for suppressing non-maxima pixels
		return self;

	def linkEdgeSeg(self, noisierImage):
		# Placeholder for linking edge segments
		return self;

	def findEdges(self):
		# Placeholder edge detection - Canny Edge Detection Method
		self.enhance();
		self.findGradient();
		self.applyThreshold(self, T);
		self.suppress();
		self.applyThreshold(self, T1);
		self.applyThreshold(self, T2);
		self.linkEdgeSeg();
		return self;


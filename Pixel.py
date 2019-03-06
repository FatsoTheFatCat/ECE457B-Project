from Rgb import Rgb

# The Pixel class is simply a structure used to hold the information associated with an image pixel together in an object

# Class Members:
#		x - The x-coordinate of the pixel within an Image
#		y - The y-coordinate of the pixel within an Image
#		rgb - An Rgb object that holds the RGB data of the pixel

# Methods:
#		getX - Returns the x-coordinate of the Pixel.
#		setX - Assigns the given parameter as the x-coordinate of the Pixel.
#		getY - Returns the y-coordinate of the Pixel.
#		setY - Assigns the given parameter as the y-coordinate of the Pixel.
#		getRGBdata - Returns an Rgb object with the RGB data for the Pixel.
#		setRgb - Assigns the given parameter as the RGB data of the Pixel.
#		setRedGreenBlue - Takes three parameters representing the red, green, and blue values and assigns them as the RGB data of the Pixel.

class Pixel:
	x = 0;
	y = 0;
	rgb = None;

	def __init__(self, x, y):
		self.x = x;
		self.y = y;

	def getX():
		return self.x;

	def setX(x):
		self.x = x;

	def getY():
		return self.y;

	def setY(y):
		self.y = y;

	def getRGBdata():
		return self.rgb;

	def setRgb(rgb):
		self.rgb = rgb;

	def setRedGreenBlue(r, g, b):
		self.setRgb(Rgb(r, g, b));

# The Rgb class is simply a structure used to hold the RGB data together in an Object

# Class Members:
#		red - A value between 0 and 255 representing the amount of red
#		green - A value between 0 and 255 representing the amount of green
#		blue - A value between 0 and 255 representing the amount of blue

# Methods:
#		getRed - Returns the redness of the object.
#		setRed - Assigns the redness of the object if the given parameter is a valid redness between 0 and 255.
#					 - Returns a boolean representing whether the assignment occured.
#		getGreen - Returns the greenness of the object.
#		setGreen - Assigns the greenness of the object if the given parameter is a valid greenness between 0 and 255.
#						 - Returns a boolean representing whether the assignment occured.
#		getBlue - Returns the blueness of the object.
#		setBlue - Assigns the blueness of the object if the given parameter is a valid blueness between 0 and 255.
#						- Returns a boolean representing whether the assignment occured.

class Rgb:
	red = 0;
	green = 0;
	blue = 0;

	def __init__(self, r, g, b):
		self.setRed(r);
		self.setGreen(g);
		self.setBlue(b);

	def getRed():
		return self.red;

	def setRed(r):
		if (r >= 0 and r <= 255):
			self.red = r;
			return True;
			
		return False;

	def getGreen():
		return self.green;

	def setGreen(g):
		if (g >= 0 and g <= 255):
			self.green = g;
			return True;
			
		return False;

	def getBlue():
		return self.blue;

	def setBlue(b):
		if (b >= 0 and b <= 255):
			self.blue = b;
			return True;

		return False;
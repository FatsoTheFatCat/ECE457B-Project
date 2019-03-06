from Image import Image

# The Light class inherits from the Image class.
# Therefore, this Light class is an Image. 
# It represents information associated with the Lights or circles on a Traffic Light.

# Class Members:
#		arrow - Indicates whether this Light is shaped as an arrow or not.
#		blinking - Indicates whether this Light is blinking.
#		on - Identifies whether this Light is lit. 

#		isOn - Returns the state of the Light.
#		setOn - Manually sets the state of the Light.
#		isArrow - Returns whether the shape of the Light is an arrow. 
#		isBlinking - Returns whether this Light is blinking.

class Light(Image):
	arrow = False;
	blinking = False;
	on = False;

	def __init__(self, rows, cols):
		Image.__init__(self, rows, cols);

	def isOn():
		return self.on;

	def setOn(on):
		self.on = on;

	def isArrow():
		return self.arrow;

	def isBlinking():
		return self.blinking;
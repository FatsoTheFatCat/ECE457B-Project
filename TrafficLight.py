from Image import Image

# The Traffic Light class inherits from the Image class. 
# Therefore, this Traffic Light class is an Image.
# It is meant to represent the information associated with a traffic light.

# Class Members:
#		numLights - The number of lights or "circles" in the traffic light.
#							- Defaults to the more common style of traffic light with 3 lights.
#							- Valid numbers are 3 and 4.
#		colour - The colour lit up on the traffic light.
#					 - Valid colours are red, yellow, green, and black.

# Methods:
#		processNumLights - Checks the Traffic Light Image for the number of Lights (or circles) on the Traffic Light.
#										 - Automatically sets the numLights member.
#		getNumLights - Returns the number of Lights on the Traffic Light.
#		setNumLights - Assigns the number of Lights on the Traffic Light if a valid number is given as the parameter.
#								 - For this project, the only valid number of Lights on the Traffic Light are 3 and 4.
#		processColour - Identifies the colour of the lit up Light on the Traffic Light.
#									- Automatically sets the colour member. 
#									- If none of the Lights are lit, the colour member is set to none.
#		getColour - Returns the colour of the lit up Light on the Traffic Light.
#		setColour - Assings, the colour of the Light on the Traffic Light if a valid colour is given as the parameter.
#							- Valid parameters are 'r' representing red, 'y' representing yellow, 'g' representing green, or 'n' representing none

class TrafficLight(Image):
	numLights = 3;
	colour = None;

	def __init__(self, rows, cols):
		Image.__init__(self, rows, cols);

	def processNumLights():
		# Placeholder processor for counting number of lights
		pass;

	def getNumLights():
		processNumLights();
		return self.numLights;

	def setNumLights(lights):
		if (lights == 3 or lights == 4):
			self.numLights = lights;
			return True;

		return False;

	def processColour():
		# Placeholder processor for determining colour
		pass;

	def getColour():
		processColour();
		return self.colour;
		
	def setColour(colour):
		if (colour == 'r' or colour == 'y' or colour == 'g' or colour == 'n'):
			self.colour = colour;
			return True;

		return False;
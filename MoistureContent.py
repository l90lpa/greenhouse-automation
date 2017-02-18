

import ADConverter
import time

class MoistureContent:
	'Read moisture content from sensor'

	def __init__(self, channel):
		self.channel = channel
		self.data = []
		self.value = 0

	# Return currently held average MC reading
	def read(self):
    	return self.value
    	
    	
    # Take seven new readings from MC sensor through ADC chip and return average	
	def updateRead(self):
		self.data = []
		for i in range(0, 6):
			self.data.append(int(ADConverter.readChannel(self.channel)))
			time.sleep(30)
		temp = 0
		for i in self.data:
			temp += i
		self.value = temp / len(self.data)
    	return self.value
      
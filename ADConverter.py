

import spidev

# Write the read command. The actual command is 17 bits but only whole bytes can be sent
# so the command starts with 7 padding zeros at the start to make it up to 24 bits(3bytes):
# 7 padding zeros,
# start bit (1),
# single ended selection bit (1),
# three bits to select the channel (XXX), channel range from 0 to 7
# remainder, 12 zeros to cover the two bits padding and ten bits for the data.
# Each byte is then stored separately in an array.
def writeReadCommand(channel):
	startBit = 0x01
	singleEnded = 0x80
	return [startBit, singleEnded | (channel << 4), 0x00]

# Neglect first byte, capture last 10 bits		
def processOutput(output):
    byteTwo = (output[1] & 0x03)
    byteThree = output[2]
    return (byteTwo << 8 | byteThree) 

# returns the 10-bit number   	  
def readChannel(channel);
   	if ((channel > 7) or (channel < 0)):
		return -1
	output = spi.xfer2(writeReadCommand(channel))
	return processOutput(output)
	
       


import time
import MoistureContent
import DBInterface
import RPi.GPIO



# MCP3008 channel
ch1 = 1
# Limit at which to water plants
MCLimit = 500
# MC Sensor object for reading values
MCSensor = MoistureContent.MoistureContent(ch1)
# Database object for storing data
DB = DBInterface.DB('garden')
# GPIO setup
RPi.GPIO.setmode(RPi.GPIO.BCM)

# open and close valve for some set period
def waterPlants():
	RPi.GPIO.setmode(16, RPi.GPIO.OUT)
	RPi.GPIO.output(16, RPi.GPIO.HIGH)
	time.sleep(60)
	RPi.GPIO.output(16, RPi.GPIO.LOW)
	
# Check moisture content every hour and water when necessary
while True:
	dateTimeGroup = time.localtime(time.time())
	currentTime = "%i:%i" % (dateTimeGroup[3],dateTimeGroup[4])
	currentDate = "%i-%i-%i" % (dateTimeGroup[0],dateTimeGroup[1],dateTimeGroup[2])
	
	watered = "false"
	
	if (MCSensor.updateRead() < MCLimit):
		waterPlants()
		watered = "true"
	
	data = [currentTime,currentDate,MCSensor.read(),-100,watered]
	
	DB.insertRow(data)
	
	time.sleep(3600)
	
#Socket client for Smarter Coffee machine
 
import socket   #for sockets
import sys  #for exit
from array import array
#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print "Failed to create socket"
    sys.exit()
     
print "Socket Created"
 
host = "192.168.1.176";
port = 2081;
buffer = 20

returnMessageType = {
	'0x0' : "Ok",
	'0x1' : "Error: Brewing",
	'0x2' : "Error: No carafe",
	'0x3' : "Error: Not enough water",
	'0x4' : "Error: You sent wrong value",
}

#Connect to remote server
s.connect((host , port))


def coffeeSetCupsFunc(number): #cups value can be between 1 - 12. Syntax for cups is 36xx7e where 36 is value for "set cups" xx is how many and 7e is packet terminator
	cupsHex = ""
	if number <= 12 and number >= 1:
		cupsHex = "%0.2X" % number # convert to hex
	else:
		print "Error: coffe cups must be a value between 1 - 12 autosetting 1 cup"
		cupsHex = "01"
	coffeeSetCups = "36" + cupsHex + "7e"
	return coffeeSetCups
	
def coffeeSetStrengthFunc(numberStrength): # strength value can be between 1 - 3
	strenghtHex = ""
	if numberStrength >= 1 and numberStrength <= 3:
		strengthHex = "%0.2X" % numberStrength # convert to hex
	else:
		print "Error: coffe strength must be a value between 1 - 3 autosetting 1"
		strengthHex = "01"
	coffeeSetStrength = "35" + strengthHex + "7e"
	return coffeeSetStrength
	
def coffeeStartFunc(cupsStart, strenghtStart, grindStart, hotPlateTime): #cupsStart = how many cups will be made max 12 min 1, 01 - 09 10 = 0a 11 = 0b 12 = 0c. strenghtStart = how strong the coffe will be 00 - 02. grindStart = 01 = on 00 = off (grinder, filter). hotPlateTime = how long the hotplate will stay on after finished brewing minimum 5min 
	cupsHex = ""
	strenghtHex = ""
	grindHex = ""
	hotPlateHex = ""
	if cupsStart <= 12 and cupsStart >= 1:
		cupsHex = "%0.2X" % cupsStart # convert to hex
	else:
		print "Error: coffe cups must be a value between 1 - 12 autosetting 1 cup"
		cupsHex = "01"
		
	if strenghtStart >= 1 and strenghtStart <= 3:
		strengthHex = "%0.2X" % strenghtStart # convert to hex
	else:
		print "Error: coffe strength must be a value between 1 - 3 autosetting 1"
		strengthHex = "01"	
		
	if grindStart == 1:
		grindHex = "01"
	else:
		grindHex = "00"
		
	if hotPlateTime < 5:
		print "Error: Time must be minimum 5. Autosetting 5min"
		hotPlateHex = "05"
	else:
		hotPlateHex = "%0.2X" % hotPlateTime # convert to hex
		
	finalHex = "33" + cupsHex + strengthHex + hotPlateHex + grindHex + "7e"
	return finalHex
	
def coffeeHotPlate(timeValue): #Timevalue is for how long the hot plate will be on before auto turning off. Lowest value is 5 min. Max value is ?
	hotPlateHex = ""
	if timeValue < 5:
		print "Error: Time must be minimum 5. Autosetting 5min"
		hotPlateHex = "3e057e"
	else:
		timeValue = "%0.2X" % timeValue # convert to hex
		hotPlateHex = "3e" + timeValue + "7e"
	return hotPlateHex

def coffeeStartWithCurrentSettings():
	return "37"

def sendCommand(valueSend):
	s.send(valueSend.decode('hex'))
	
def returnMessage(incomingData):
	a = array("B", incomingData)		
	b = map(hex, a)
	print b
	returnMessage = b[1]
	print "Return: " + returnMessageType[returnMessage]
		
	
sendCommand(coffeeSetCupsFunc(6)) # Send command
returnMessage(s.recv(buffer)) # display return message
s.close

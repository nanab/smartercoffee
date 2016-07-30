#Socket client for Smarter Coffee machine
 
import socket   #for sockets
import sys  #for exit
from array import array
incommingCommandSecond = ""
incommingCommandFirst = ""
#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
     
print 'Socket Created'
 
host = '192.168.0.86';
port = 2081;
statusMessageType = {
	'0x4' : "Filter, ?",
	'0x5' : "Filter, OK to start",
	'0x6' : "Filter, OK to start",
	'0x7' : "Beans, OK to start",
	'0x20' : "Filter, No carafe",
	'0x22' : "Beans, No carafe",
	'0x45' : "Filter, Done",
	'0x47' : "Beans, Done",
	'0x53' : "Boiling",
	'0x60' : "Filter, No carafe, Hotplate On",
	'0x61' : "Filter, Hotplate On",
	'0x62' : "Beans, No carafe, Hotplate On",
	'0x63' : "Beans, Hotplate On",
	'0x51' : "Descaling in progress",
	
}
waterLevelMessageType = {
	'0x0' : "Not enough water",
	'0x1' : "Low",
	'0x2' : "Half",
	'0x12' : "Half",
	'0x13' : "Full",		
}
strengthMessageType = {
	'0x0' : "weak",
	'0x1' : "medium",
	'0x2' : "strong",		
} 
cupsMessageType = { #TODO investigate what the first number does?
	'0x61' : "1",
	'0x62' : "2",
	'0x63' : "3",
	'0x64' : "4",
	'0x65' : "5",
	'0x66' : "6",
	'0x67' : "7",
	'0x68' : "8",
	'0x69' : "9",
	'0x6a' : "10",
	'0x6b' : "11",
	'0x6c' : "12",
	'0x81' : "1",
	'0x82' : "2",
	'0x83' : "3",
	'0x84' : "4",
	'0x85' : "5",
	'0x86' : "6",
	'0x87' : "7",
	'0x88' : "8",
	'0x89' : "9",
	'0x8a' : "10",
	'0x8b' : "11",
	'0x8c' : "12",
	'0x21' : "1",
	'0x22' : "2",
	'0x23' : "3",
	'0x24' : "4",
	'0x25' : "5",
	'0x26' : "6",
	'0x27' : "7",
	'0x28' : "8",
	'0x29' : "9",
	'0x2a' : "10",
	'0x2b' : "11",
	'0x2c' : "12",
	'0xc1' : "1",
	'0xc2' : "2",
	'0xc3' : "3",
	'0xc4' : "4",
	'0xc5' : "5",
	'0xc6' : "6",
	'0xc7' : "7",
	'0xc8' : "8",
	'0xc9' : "9",
	'0xca' : "10",
	'0xcb' : "11",
	'0xcc' : "12",
}
 
#Connect to remote server
s.connect((host , port))
 
print 'Socket Connected to ' + host + ' on ip ' + host
while 1:
	reply = s.recv(4096)
	incommingCommandFirst = reply
	if incommingCommandFirst == incommingCommandSecond: # only display message if something is changed
		pass
	else:
		incommingCommandSecond = reply		
		a = array("B", reply)		
		b = map(hex, a)
		deviceMessage = b[0]
		statusMessage = b[1]
		waterLevelMessage = b[2]
		wifiStrenghtMessage = b[3]
		strengthMessage = b[4]
		cupsMessage = b[5]
		print
		print 'Status:', statusMessageType[statusMessage]
		print 'WaterLevel:', waterLevelMessageType[waterLevelMessage]
		print 'Strength:', strengthMessageType[strengthMessage]
		print 'Cups:', cupsMessageType[cupsMessage]




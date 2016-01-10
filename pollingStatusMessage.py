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
 
host = '192.168.1.176';
port = 2081;
statusMessageType = {
	'0x4' : "Filter, ?",
	'0x5' : "Grinder, ?",
	'0x6' : "Filter, OK to start",
	'0x7' : "Grinder, OK to start",
	'0x20' : "Filter, No carafe",
	'0x22' : "Grinder, No carafe",
	'0x45' : "Filter, Done",
	'0x47' : "Grinder, Done",
	'0x53' : "Boiling",
	'0x60' : "Filter, No carafe, Hotplate On",
	'0x61' : "Filter, Hotplate On",
	'0x62' : "Grinder, No carafe, Hotplate On",
	'0x63' : "Grinder, Hotplate On",
	
}
waterLevelMessageType = {
	'0x2' : "Not enough water",
	'0x12' : "Half",
	'0x13' : "Full",		
}
strenghtMessageType = {
	'0x0' : "1",
	'0x1' : "2",
	'0x2' : "3",		
} 
cupsMessageType = {
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
		#print b
		deviceMessage = b[0]
		statusMessage = b[1]
		waterLevelMessage = b[2]
		wifiStrenghtMessage = b[3]
		strenghtMessage = b[4]
		cupsMessage = b[5]
		print "Status: " + statusMessageType[statusMessage] + " ,WaterLevel: " + waterLevelMessageType[waterLevelMessage] + " ,Strenght: " + strenghtMessageType[strenghtMessage] + " ,Cups: " + cupsMessageType[cupsMessage]
		
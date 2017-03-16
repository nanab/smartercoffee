#Socket client for Smarter Coffee machine

import socket   #for sockets
import sys  #for exit
from array import array
import argparse

# Accept and parse notify arguments
parser = argparse.ArgumentParser()
parser.add_argument('--notify', action='store', \
                    choices=['GNOME'], \
                    help='Select notify mode')

try:
    command_line = parser.parse_args()
except:
    sys.exit(2)

if command_line.notify == 'GNOME':
    from gi.repository import Notify
    Notify.init("Gnome")

incommingCommandSecond = ""
incommingCommandFirst = ""
#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    if command_line.notify == 'GNOME':
        Gnome =  Notify.Notification.new("Smarter Coffee", "Failed to create coffee socket")
        Gnome.show()
    else:
        print 'Failed to create socket'
    sys.exit()

if command_line.notify == None:
    print 'Socket Created'

host = '192.168.1.15'
port = 2081
statusMessageType = {
    '0x4' : "Filter, ?",
    '0x5' : "Filter, OK to start",
    '0x6' : "Filter, OK to start",
    '0x7' : "Beans, OK to start",
    '0x20' : "Filter, No carafe",
    '0x22' : "Beans, No carafe",
    '0x23' : "Beans, Not enough water",
    '0x45' : "Filter, Done",
    '0x46' : "Beans, No carafe, Hotplate On",
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
    '0x1' : "1",
    '0x2' : "2",
    '0x3' : "3",
    '0x4' : "4",
    '0x5' : "5",
    '0x6' : "6",
    '0x7' : "7",
    '0x8' : "8",
    '0x9' : "9",
    '0xa' : "10",
    '0xb' : "11",
    '0xc' : "12",
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
    '0x31' : "1",
    '0x32' : "2",
    '0x33' : "3",
    '0x34' : "4",
    '0x35' : "5",
    '0x36' : "6",
    '0x37' : "7",
    '0x38' : "8",
    '0x39' : "9",
    '0x3a' : "10",
    '0x3b' : "11",
    '0x3c' : "12",
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
s.connect((host, port))

if command_line.notify == None:
    print 'Socket Connected to ' + host + ' on ip ' + host

while 1:
    reply = s.recv(4096)
    incommingCommandFirst = reply
    if incommingCommandFirst != incommingCommandSecond: # only display message if something is changed
        c = array("B", incommingCommandSecond)
        incommingCommandSecond = reply
        a = array("B", incommingCommandSecond)
        b = map(hex, a)
        deviceMessage = b[0]
        statusMessage = b[1]
        waterLevelMessage = b[2]
        wifiStrenghtMessage = b[3]
        strengthMessage = b[4]
        cupsMessage = b[5]

        try:
            textMessageStatus = 'Status: ' + statusMessageType[statusMessage]
        except:
            textMessageStatus = 'Status: Unknown (' + statusMessage +')'
    
        try:
            textMessageWater = 'Water Level: ' + waterLevelMessageType[waterLevelMessage]
        except:
            textMessageWater = 'Water Level: Unknown (' + waterLevelMessage +')'

        try:
            textMessageStrength = 'Strength: ' + strengthMessageType[strengthMessage]
        except:
            textMessageStrength = 'Strength: Unknown (' + strengthMessage +')'

        try:
            textMessageCups = 'Cups: ' + cupsMessageType[cupsMessage]
        except:
            textMessageCups = 'Cups: Unknown (' + cupsMessage +')'

        if command_line.notify == 'GNOME':

            if len(c) > 0:
                if a[1] != c[1]:
                    Gnome = Notify.Notification.new("Smarter Coffee", textMessageStatus)
                    Gnome.show()
                if a[2] != c[2]:
                    Gnome = Notify.Notification.new("Smarter Coffee", textMessageWater)
                    Gnome.show()
                if a[4] != c[4]:
                    Gnome = Notify.Notification.new("Smarter Coffee", textMessageStrength)
                    Gnome.show()
                if a[5] != c[5]:
                    Gnome = Notify.Notification.new("Smarter Coffee", textMessageCups)
                    Gnome.show()
            else:
                Gnome = Notify.Notification.new("Smarter Coffee", \
                                        "Socket created and connected to " + host + "\n" + \
                                        textMessageStatus + "\n" + \
                                        textMessageWater + "\n" + \
                                        textMessageStrength + "\n" + \
                                        textMessageCups)
                Gnome.show()

        else:
            print
            print textMessageStatus
            print textMessageWater
            print textMessageStrength
            print textMessageCups

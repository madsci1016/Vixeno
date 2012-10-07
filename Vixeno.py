#  Bill's Super Awesome Vixen to Arduino/AVR/C script
#		www.billporter.info
#
#	This script parses a Vixen Sequence file and outputs a .cpp file with an array
#      of the data that makes up the actual sequence; formatted for Arduino/AVR microcontrollers.
#      Use it to embed short light shows in your next Arduino project.
# 
#	Make sure you call this script with the vixen sequence filename you want to 
#   convert as an argument. Like this: 
#			path>python Vixeno.py show.vix
#
import base64
import sys
from xml.dom import minidom

filein = sys.argv[1]

print ('Opening %s ' % filein)
#open and parse Vixen file
xmldoc = minidom.parse(filein)
itemlist = xmldoc.getElementsByTagName('EventValues')
vixenshow = itemlist[0].childNodes[0].nodeValue
# print (itemlist[0].childNodes[0].nodeValue)

itemlist = xmldoc.getElementsByTagName('Channel') 
channels = len(itemlist)

itemlist = xmldoc.getElementsByTagName('EventPeriodInMilliseconds')
frameduration = itemlist[0].childNodes[0].nodeValue

#decode base64 endoding. Result is binary
vixenbinary = base64.b64decode(vixenshow)
#breakup binary string to array
outputarray = list(vixenbinary)
# convert binary elements to decimal
outputarray = [ord(c) for c in outputarray]

#figure out number of samples in the show
samples = len(outputarray) / channels

print('Found %d Channels and %d frames for %d total bytes of memory' % (channels, samples, channels*samples))

#start creating output file
fileout = open('VixenShow.cpp', 'w')
fileout.write('#include <avr/pgmspace.h> \n \n')
fileout.write('static uint8_t vixen_channels = %s; \n' % str(channels))
fileout.write('static uint16_t vixen_frames = %s; \n' % str(samples))
fileout.write('static uint16_t vixen_frameduration = %s; \n \n' % str(frameduration))
fileout.write('static PROGMEM prog_uint8_t vixen_show_data[')
fileout.write(str(channels))
fileout.write('][')
fileout.write(str(samples))
fileout.write('] = { ')

for i in range(channels):
	fileout.write('\n')
	fileout.write('{')
	for x in outputarray[samples*i:samples*i+samples]:
		fileout.write(str(x))
		fileout.write(',')
	fileout.seek(-1, 1)
	fileout.write('},')
fileout.seek(-1, 1)
fileout.write('};')

fileout.close()



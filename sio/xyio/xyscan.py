# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import math

import bluetooth._bluetooth as bluez
bdev ="00:eb:19:00:b7:b9"
minor = sys.argv[1] #30979 47033 15107
dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------"
	for beacon in returnedList:
		if beacon.split(',')[3]==minor:
			txCalebPow= int(beacon.split(',')[4])
			rssi = int(beacon.split(',')[5])
			ratioDb = (txCalebPow - rssi)
			ratioLin = math.pow(10, ratioDb / 10.0)
			rm = math.sqrt(ratioLin)
			rf = round(3.2808*rm) 
			print "%d feet, Db difference is %d, power ratio is 1/%d" % (rf , ratioDb, ratioLin)

			print beacon


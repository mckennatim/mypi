# test BLE Scanning software
# jcs 6/8/2014
import time
import blescan
import sys
import math
from flask import jsonify

import bluetooth._bluetooth as bluez


#minor = sys.argv[1] #30979 47033 15107

def xy(minor):	
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
		pollBLE(sock,minor)
		# returnedList = blescan.parse_events(sock, 10)
		# print "----------"
		# for beacon in returnedList:
		# 	if beacon.split(',')[3]==minor:
		# 		txCalebPow= int(beacon.split(',')[4])
		# 		rssi = int(beacon.split(',')[5])
		# 		ratioDb = (txCalebPow - rssi)
		# 		ratioLin = math.pow(10, ratioDb / 10.0)
		# 		rm = math.sqrt(ratioLin)
		# 		rf = round(3.2808*rm) 
		# 		print "%d feet, Db difference is %d, power ratio is 1/%d" % (rf , ratioDb, ratioLin)

		# 		print beacon

def pollBLEjson(sock, minor):
	returnedList = blescan.parse_events(sock, 10)
	#print "----------"
	for beacon in returnedList:
		if beacon.split(',')[3]==minor:
			txCalebPow= int(beacon.split(',')[4])
			rssi = int(beacon.split(',')[5])
			ratioDb = (txCalebPow - rssi)
			ratioLin = math.pow(10, ratioDb / 10.0)
			rm = math.sqrt(ratioLin)
			rf = round(3.2808*rm) 
			#message=  "%d feet, Db difference is %d, power ratio is 1/%d on beacon %s" % (rf , ratioDb, ratioLin, minor)
			mdict=  dict([('message', 'reporting'),('beacon', minor), ('distance', rf), ('dBdiff', ratioDb), ("powerRatio", ratioLin) ])
			message = jsonify(mdict)
			return message
	return "that beacon is not reporting"	

def pollBLE(sock, minor):
	returnedList = blescan.parse_events(sock, 10)
	#print "----------"
	for beacon in returnedList:
		if beacon.split(',')[3]==minor:
			txCalebPow= int(beacon.split(',')[4])
			rssi = int(beacon.split(',')[5])
			ratioDb = (txCalebPow - rssi)
			ratioLin = math.pow(10, ratioDb / 10.0)
			rm = math.sqrt(ratioLin)
			rf = round(3.2808*rm) 
			message=  "%d feet, Db difference is %d, power ratio is 1/%d on beacon %s" % (rf , ratioDb, ratioLin, minor)
			return message
	return "that beacon is not reporting"	
	
def pollAll(sock):
	returnedList = blescan.parse_events(sock, 10)
	print "----------"
	bigmess= ""
	for beacon in returnedList:
		minor= int(beacon.split(',')[3])
		if int(minor > 1):
			txCalebPow= int(beacon.split(',')[4])
			rssi = int(beacon.split(',')[5])
			ratioDb = (txCalebPow - rssi)
			ratioLin = math.pow(10, ratioDb / 10.0)
			rm = math.sqrt(ratioLin)
			rf = round(3.2808*rm) 
			message=  "%d feet, Db difference is %d, power ratio is 1/%d on beacon %s \n %s \n" % (rf , ratioDb, ratioLin, minor, beacon)
			bigmess += message
	return bigmess

def setup():
	dev_id = 0
	try:
		sock = bluez.hci_open_dev(dev_id)
		print "ble thread started"

	except:
		print "error accessing bluetooth device..."
	    	sys.exit(1)

	blescan.hci_le_set_scan_parameters(sock)
	blescan.hci_enable_le_scan(sock)
	return sock	

def whichBeacon():
	return "47033"

def yeahWhat():
	time.sleep(10)
	return "so what"

import xymod

sock = xymod.setup()
minor = xymod.whichBeacon()
while True:
	message= xymod.pollBLE(sock,minor)
	print message


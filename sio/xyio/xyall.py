import xymod

sock = xymod.setup()
while True:
	message= xymod.pollAll(sock)
	print message


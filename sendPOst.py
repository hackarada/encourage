import requests
import serial
import random
import time

print("#####################################################################################")
ser = serial.Serial('/dev/tty.usbmodem1411', 9600)

while True:
	
	print("sending Vital Data")
	print ser.write('1')

	#print ser.read();
	tempData = random.randrange(32,46)
	hbdata = random.randrange(20,200)
	bpdata = str(random.randrange(2,10)) + "/" + str(random.randrange(100,200))


	#r = requests.post("localhost", data={'temp': tempData, 'hb': hbdata, 'bp': '100/100'})

	#print(r.status_code, r.reason)

	time.sleep(3)
	print ser.write('2')
	print "Finished Sending"
	print("Server Updated With Current Data")

	time.sleep(10)


import requests
import serial
import random
import time

print("#------------------------------------------------------------------------------------------------#\n\r")
print("#----------------- Sew realTime Vital Monitoring and Tracking -----------------------------------#")
print("#------------------------------------------------------------------------------------------------#\n\r")
 
try:
	print("+ Locating Sensor ...")
	ser = serial.Serial('/dev/serial/by-path/platform-3f980000.usb-usb-0:1.2:1,0', 9600)
	#ser = serial.Serial('/dev/cu.usbmodem1421',9600)
	print("+ Finished Connection With Sensor device!!")

	while True:
		print("--------------------------------------------------------------------------------------------------\n\r")
		print("+ Sending Vital Data To Server at ttp://35.184.140.98 ")
	  ser.write('1')
		print ser.readline()
		tempData = random.randrange(32,46)
		hbdata = random.randrange(20,200)
		bpdata = str(random.randrange(2,10)) + "/" + str(random.randrange(100,200))
		r = requests.post("http://35.184.140.98/api/patient/", data={'temp': tempData, 'hb': hbdata, 'bp': bpdata})
		print(r.status_code, r.reason)
		time.sleep(4)
		ser.write('2')
		print ser.readline()
		print "+ Finished Sending Data - Server Updated With Current Data - " + time.asctime(time.localtime(time.time()))
		print("--------------------------------------------------------------------------------------------------\n\r")

		time.sleep(2)

except Exception, e:
 	print(" ^^ Error ",e.args)
 	print e.args

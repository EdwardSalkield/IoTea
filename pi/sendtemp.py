import RPi.GPIO as GPIO
import time
from w1thermsensor import W1ThermSensor

GPIO.setmode(GPIO.BCM)

datapins = [14, 15, 18, 23, 24, 25, 8]

for d in datapins:
	GPIO.setup(d, GPIO.OUT)

# Set up temperature sensor
sensor = W1ThermSensor()


def getTemperature():
	temp = int(sensor.get_temperature())
	binstr = bin(temp)[2:]
	padding = (7-len(binstr))*'0'
	binstr = padding + binstr
	print(temp)
	print(binstr)
	i = 0

	pins = []
	for c in binstr:
		if c == '1':
			pins.append(datapins[i])
		i+=1

	GPIO.output(datapins, 0)
	GPIO.output(pins, 1)

while True:
	getTemperature()
	time.sleep(1)

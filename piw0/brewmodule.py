#!/usr/bin/python3
# Input
# ./brew mode temperature time leaf

import time
import sys
import control

# Calibration
# Time for 20 rotations - 34.1 clockwise
#			36.5
POURTIME = 5
POURTIME2 = 5

CWANGLE = 50
ACWANGLE = -63

actu = {'kettle': 0, 'brew': [1,2,3,4]}

def pour(b):
	for a in actu['brew']:
		control.actuator(a, b)

def brew(temperature, brewtime):
	# Turn on the kettle
	print("Kettle on")
	control.actuator(actu['kettle'], False)

	# Wait for the correct temperature
	print("Waiting for correct temperature")
	boiled = False
	while not boiled:
		t = control.getTemperature()
		print("Current temperature: " + str(t))
		if t >= temperature:
			boiled = True

	# Stop boiling the kettle
	print("Kettle boiled")
	control.actuator(actu['kettle'], True)

	# Dispense the water
	print("Water dispensed")
	control.movebyangle(CWANGLE)
	time.sleep(POURTIME)
	control.movebyangle(ACWANGLE)

	# Brew the tea
	print("Brewing tea")
	time.sleep(brewtime)

	# Dispense the tea
	print("Dispensing tea")
	pour(True)

	time.sleep(POURTIME2)

	pour(False)
	print("Enjoy your cuppa")

def rinse():
	# Dispense the water
	print("Water dispensed")
	control.movebyangle(CWANGLE)
	time.sleep(POURTIME)
	control.movebyangle(ACWANGLE)

	# Dispense the tea
	print("Dispensing tea")
	pour(True)

	time.sleep(POURTIME2)
	pour(False)

	print("Teaware rinsed")



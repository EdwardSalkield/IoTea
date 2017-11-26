import RPi.GPIO as GPIO
import time
from w1thermsensor import W1ThermSensor

# Calibration
CWROT = 1.7
AWROT = 1.8

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up servo controls
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)
pwm.start(0)

# Set up actuators
actu = {0:17, 1: 27, 2:22, 3:14, 4:15}
for v in actu.values():
    GPIO.setup(v, GPIO.OUT)

# Set up data pins
datapins = [10, 9, 11, 5, 6, 13, 19][::-1]
for d in datapins:
    GPIO.setup(d, GPIO.IN)

# Set up temperature sensor
#sensor = W1ThermSensor()

# 0 - still
# 1 - clockwise
# -1 - anticlockwise
def moveservo(i):
	duty = 0.0
	if i == 0:
		duty = 0.0
		print("Stopping")
	elif i == 1:
		duty = 8.0
		print("Clockwise")
	elif i == -1:
		duty = 6.0
		print("Anticlockwise")

	pwm.ChangeDutyCycle(duty)

def movebyangle(angle):
	rot = (angle/360)*2
	print("Rotating for " + str(rot) + " circles")
	if angle > 0:
		t = rot*CWROT
		moveservo(1)
	else:
		t = rot*AWROT
		moveservo(-1)

	time.sleep(abs(t))
	moveservo(0)

	

# Changes actuator i state to b
def actuator(i, b):
	state = int(b)
	GPIO.output(actu[i], state)
	print("Changed actuator state")

def getTemperature():
    # Convert the current pins into an int
    n = 0
    binary = ''
    for i in range (0, 7):
        inp = GPIO.input(datapins[i])

        if inp:
            n += pow(2, i)

    return n


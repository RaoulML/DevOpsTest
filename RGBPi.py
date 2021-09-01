import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

RUNNING = True

green = 27
red = 17
blue = 22

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

Freq = 100

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)

try:
        RED.start(0)
        GREEN.start(0)
        BLUE.start(0)
	while RUNNING:
	        # Lighting up the RGB led. 100 means giving 100% to the pin


		for x in range(0,101):
			GREEN.ChangeDutyCycle(x) # Changes the with of the PWM duty cycle
			time.sleep(0.05)
		for x in range(0,101):
			RED.ChangeDutyCycle(100-x)
			time.sleep(0.025)
		for x in range(0,101):
			GREEN.ChangeDutyCycle(100-x)
			BLUE.ChangeDutyCycle(x)
			time.sleep(0.025)
		for x in range(0,101):
			RED.ChangeDutyCycle(x)
			time.sleep(0.025)
except KeyboardInterrupt:
	# Gracefully exit the RGB lighting loop in order to shut down the lights
	RUNNING = False
	GPIO.cleanup()

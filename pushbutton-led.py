
# Module imports
import RPi.GPIO as GPIO
import time

# Using the GPIO ports
GPIO.setmode(GPIO.BCM)

# Remove warning messages
GPIO.setwarnings(False)

# Pin variables
led_pin = 18
button_pin = 17

# Setup pins
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #give the input a default value, i.e 0

# Main function
def led():
	GPIO.output(led_pin, GPIO.HIGH)
	print("The LED should be on.")
	time.sleep(1) #1 second delay

	GPIO.output(led_pin, GPIO.LOW)
	print("The LED should be off.")

	GPIO.cleanup()

# Light LED using the switch
def pushbutton():
	try:
		GPIO.add_event_detect(button_pin, GPIO.BOTH)
		while True:
			if(GPIO.event_detected(button_pin)):
				GPIO.output(led_pin, not GPIO.input(button_pin))
			time.sleep(0.1)
	finally:
		GPIO.output(led_pin, GPIO.LOW)
		GPIO.cleanup()

# Execute the functions
if __name__ == "__main__":
	pushbutton()

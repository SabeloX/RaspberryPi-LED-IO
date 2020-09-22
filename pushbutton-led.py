# Module imports
import RPi.GPIO as GPIO
import time

# Using the GPIO ports
GPIO.setmode(GPIO.BCM)

# Remove warning messages
GPIO.setwarnings(False)

# Pin variables
led_pin = 17
button_pin = 27

# Setup pins
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

# Main function
def main():
	GPIO.output(led_pin, GPIO.HIGH)
	print("The LED should be on.")
	time.sleep(1) #1 second delay

	GPIO.output(led_pin, GPIO.LOW)
	print("The LED should be off.")

# Execute the functions
if __name__ == "__main__":
	main()
	GPIO.cleanup() #cleaup used channels

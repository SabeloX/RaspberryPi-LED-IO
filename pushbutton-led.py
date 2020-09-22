import RPi.HPIO as GPIO

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

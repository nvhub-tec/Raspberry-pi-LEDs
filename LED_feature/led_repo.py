# led_repo.py
import RPi.GPIO as GPIO
import time

class LedRepository:
    def __init__(self, pin =26):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def led_on(self, delay=0):
        GPIO.output(26, GPIO.HIGH)  # Turn LED ON
        time.sleep(delay)

    def led_off(self, delay=0):
        GPIO.output(26, GPIO.LOW)   # Turn LED OFF
        time.sleep(delay)

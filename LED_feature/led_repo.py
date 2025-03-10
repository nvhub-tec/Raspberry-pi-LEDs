# led_repo.py
import RPi.GPIO as GPIO
import time
from LED_feature.led_repo_interface import LedInterface
# from gpiozero import LED

class LedRepository:
    def __init__(self, pin =26):
        self.pin = pin
        GPIO.setup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def led_on(self, delay=0):
        GPIO.output(26, GPIO.HIGH)  # Turn LED ON
        time.sleep(delay)

    def led_off(self, delay=0):
        GPIO.output(26, GPIO.LOW)   # Turn LED OFF
        time.sleep(delay)



class LedRepository1:
    def __init__(
        self, 
        led_service: LedInterface = Optional(LedInterface)
    ):
        self._led_service = led_service

    

            
        
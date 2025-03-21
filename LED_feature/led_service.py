# led_service.py
import random

class LedService:
    def __init__(self, led_repo):
        self.led = led_repo

    def LedBlink(self):
        while True:
            self.led.led_on(1)
            self.led.led_off(1)

    def LedSlowBlink(self):
        while True:
            self.led.led_on(5)
            self.led.led_off(5)

    def LedRandom(self):
        while True:
            self.led.led_on(random.randint(0, 7))
            self.led.led_off(random.randint(0, 7))


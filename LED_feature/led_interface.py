#led_interface.py
from LED_feature.led_service import LedService
from LED_feature.led_repo import LedRepository

def get_an_input():

    led_repo = LedRepository(26)
    led_service = LedService(led_repo)

    ledmode = led_service
    x = int(input("type '1' for blink, '2' for fast blink, and '3' for random "))
    if x == 1:
        ledmode.LedBlink()
    elif x ==2:
        ledmode.LedSlowBlink()
    elif x ==3:
        ledmode.LedRandom()

    else:
        raise TypeError("1, 2, or 3, remember?")
   
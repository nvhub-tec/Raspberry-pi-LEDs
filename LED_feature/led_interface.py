from abc import ABC, abstractmethod
from tests.LED_feature.led_service import LedService

class LedInterface:
    @abstractmethod
    def led_on(self):
        pass
    @abstractmethod
    def led_off(self):
        pass
        











# class get_an_input():
    
#     def __init__(self):

#         ledmode = LedService()

#         x = int(input("type '1' for blink, '2' for fast blink, and '3' for random "))
#         if x == 1:
#             ledmode.LedBlink()
#         elif x ==2:
#             ledmode.LedSlowBlink()
#         elif x ==3:
#             ledmode.LedRandom()

#         else:
          #  raise TypeError("1, 2, or 3, remember?")
import unittest
from unittest.mock import patch
from LED_feature.led_repo import LedRepository

class TestLedRepository(unittest.TestCase):

    @patch("led_repo.GPIO")  # Mock GPIO so it doesn’t affect hardware
    def test_led_on(self, mock_gpio):
        """Test if led_on() calls GPIO.output with HIGH"""
        led = LedRepository(18)  # Create an instance

        led.led_on()  # Call the method

        mock_gpio.output.assert_called_with(18, mock_gpio.HIGH)  # Verify correct call

    @patch("led_repo.GPIO")
    def test_led_off(self, mock_gpio):
        """Test if led_off() calls GPIO.output with LOW"""
        led = LedRepository(18)  

        led.led_off()  

        mock_gpio.output.assert_called_with(18, mock_gpio.LOW)

if __name__ == "__main__":
    unittest.main()
# My Car Projekt

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from hcsr04 import HCSR04
import utime

# Es wird I2C 0 verwendet Pin (GP0) und Pin (GP1)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

# Anzeige durch distance = sensor.distance_cm()
sensor = HCSR04(trigger_pin=2, echo_pin=3)

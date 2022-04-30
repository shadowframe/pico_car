# My Car Projekt

from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
from hcsr04 import HCSR04
# from l9110 import L9110
# import l9110
from l298 import DCMotor
from time import sleep  # need it?
import utime

button = Pin(22, Pin.IN, Pin.PULL_DOWN)
led = Pin(21, Pin.OUT)

# Es wird I2C 0 verwendet Pin (GP0) und Pin (GP1)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

# Anzeige durch distance = sensor.distance_cm()
sensor = HCSR04(trigger_pin=2, echo_pin=3)

'''
Test Funktion Button
run it on repl with:    import main1 #this file!
                        main1.test_button()
'''


def test_button():
    while True:
        if button.value() == 1:
            led.value(1)
            print("led on")
            utime.sleep(2)
            led.value(0)
            print("led off")


'''
Test OLED, HC-SR04, Button
run it on repl with:    import main1 #this file!
                        main1.test_oled()
'''


def test_oled():
    while True:
        if button.value() == 1:
            # Zeichenfläche wird geleert
            oled.fill(0)
            # An die Stelle 0, 0 wird "Hello:" geschrieben
            oled.text("MAIN", 0, 0)
            oled.show()
            # An die Stelle 10, 20 wird zusätzlich "TEST TEST TEST" geschrieben
            oled.text("TEST TEST TEST", 10, 20)
            oled.show()
            utime.sleep(2)
            # Farbe 1, 0 bestimmt die beiden invertierten Farben
            oled.fill_rect(0, 10, 128, 20, 1)
            oled.text("Jan", 10, 20, 0)
            oled.show()
            utime.sleep(2)
            # Werte vom Sensor ausgeben
            oled.fill(0)
            oled.text("DISTANCE", 0, 0)
            distance = sensor.distance_cm()
            oled.fill_rect(0, 10, 128, 20, 1)
            oled.text(str(distance) + " cm", 10, 20, 0)
            oled.show()
            utime.sleep(4)

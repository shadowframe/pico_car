from machine import UART
from l298 import DCMotor
from machine import Pin, PWM
from time import sleep
import time

# motor left
frequency = 15000
pin1 = Pin(7, Pin.OUT)
pin2 = Pin(8, Pin.OUT)
enable_l = PWM(Pin(6))

# motor right
pin3 = Pin(10, Pin.OUT)
pin4 = Pin(11, Pin.OUT)
enable_r = PWM(Pin(9))

enable_r.freq(500)
enable_l.freq(500)
dc_motor = DCMotor(pin1, pin2, pin3, pin4, enable_l, enable_r, 35000, 65535)

def test():
    for i in range(1, 3):
        print(i)

        dc_motor.forward(80)  # motor is running
        print("forward")
        time.sleep(1)

        dc_motor.stop()  # stops motor
        time.sleep(1)

        dc_motor.backwards(80)  # the motor turns in the opposite direction
        time.sleep(1)

        dc_motor.stop()  # stops motor
        time.sleep(1)

        print("left")
        dc_motor.left(10)
        time.sleep(1)

        print("right")
        dc_motor.right(10)
        time.sleep(1)

        dc_motor.stop()
        time.sleep(1)

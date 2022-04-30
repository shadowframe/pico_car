import utime
from machine import Pin, PWM

# motor left pin layout
motor1a = PWM(Pin(6))
motor1b = PWM(Pin(7))
# motor right pin layout
motor2a = PWM(Pin(8))
motor2b = PWM(Pin(9))
# freq für alle motoren einstellen
motor1a.freq(12000)
motor1b.freq(50)
motor2a.freq(50)
motor2b.freq(50)

geschwindigkeit = 40000


def motor_left():
    motor1a.duty_u16(geschwindigkeit)
    motor1b.duty_u16(0)

def los():
    while True:
        for i in range(40000, 65000, 1):
            motor1a.duty_u16(i)
            motor1b.duty_u16(0)
            print("Der Wert i: " + str(i))
            utime.sleep_ms(1)

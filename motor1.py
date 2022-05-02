from machine import Pin, PWM
from time import sleep

# Motor 1 LEFT
IN1 = Pin(7, Pin.OUT)
IN2 = Pin(8, Pin.OUT)

speed_l = PWM(Pin(6))
speed_l.freq(500)

# Motor 2 RIGHT
IN3 = Pin(10, Pin.OUT)
IN4 = Pin(11, Pin.OUT)

speed_r = PWM(Pin(9))
speed_r.freq(500)


speed = 0.5
speed_now = int(speed * 65535)

# initialisieren
IN1.low()
IN2.low()
IN3.low()
IN4.low()


def forward():
    speed_l.duty_u16(speed_now)
    IN1.low()
    IN2.high()
    speed_r.duty_u16(speed_now)
    IN3.low()
    IN4.high()

    print("forward " + str(speed_now))


def backward():
    speed_l.duty_u16(speed_now)
    IN1.high()
    IN2.low()
    speed_r.duty_u16(speed_now)
    IN3.high()
    IN4.low()


def stop():
    speed_l.duty_u16(0)
    IN1.low()
    IN2.low()
    speed_r.duty_u16(0)
    IN3.low()
    IN4.low()


def left():
    speed_l.duty_u16(0)
    IN1.low()
    IN2.low()
    speed_r.duty_u16(speed_now)
    IN3.low()
    IN4.high()


def right():
    speed_l.duty_u16(speed_now)
    IN1.low()
    IN2.high()
    speed_r.duty_u16(0)
    IN3.low()
    IN4.low()


def test():
    forward()
    sleep(2)

    stop()
    sleep(0.2)

    backward()
    sleep(3)

    stop()
    sleep(0.2)

    left()
    sleep(0.5)

    stop()
    sleep(0.2)

    right()
    sleep(0.5)

    stop()


for i in range(1, 5):
    print(i)
    test()

# while True:
#     speed_l.duty_u16(65535)
#     print("forward 65535")
#     IN1.low()  # spin forward
#     IN2.high()
#     sleep(5)
#
#     IN1.low()  # stop
#     IN2.low()
#     sleep(2)
#
#     speed_l.duty_u16(60000)
#     print("backward 60000")
#     IN1.high()  # spin backward
#     IN2.low()
#     sleep(5)
#
#     IN1.low()  # stop
#     IN2.low()
#     sleep(2)
#
#     speed_l.duty_u16(50000)
#     print("forward 50000")
#     IN1.low()  # spin forward
#     IN2.high()
#     sleep(5)
#
#     IN1.low()  # stop
#     IN2.low()
#     sleep(2)

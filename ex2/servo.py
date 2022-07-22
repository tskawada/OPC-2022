import RPi.GPIO as GPIO
from time import sleep

class Servo:
    def __init__(self):
        servo_pin = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, GPIO.OUT)
        self.servo = GPIO.PWM(servo_pin, 50)
        self.servo.start(0)

    def servo_ctrl(self, value):
        value = value * 10
        print(value)
        duty = 2.5 + (12.0 - 2.5) * (value + 90) / 180

        self.servo.ChangeDutyCycle(duty)

    def __del__(self):
        self.servo.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    serv = Servo()
    serv.servo_ctrl(-3)
    sleep(0.3)
    serv.servo_ctrl(3)
    sleep(0.3)
    del serv
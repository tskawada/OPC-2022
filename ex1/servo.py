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
    try:
        while(1):
            a = int(input("Enter the integer (-4 ~ 4): "))
            serv.servo_ctrl(a)
            sleep(0.3)
    except Exception as e:
        print(e)
        del serv
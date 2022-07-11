import RPi.GPIO as GPIO

class Servo:
    def __init__(self):
        servo_pin = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, GPIO.OUT)
        self.servo = GPIO.PWM(servo_pin, 50)

    def servo_angle(self, angle):
        duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
        self.servo.ChangeDutyCycle(duty)

    def servo_ctrl(self, value):
        value = value * 10
        mod = value % 10

        self.servo.start(0)
        if(mod != 0 or value > 40 or value < -40):
            pass
        else:
            self.servo_angle(value)
        self.servo.stop()

    def __del__(self):
        GPIO.cleanup()
import RPi.GPIO as GPIO

class DcMotor:
    def __init__(self):
        self.relay_pin = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_pin, GPIO.OUT)

    def straight(self):
        GPIO.output(self.relay_pin, False)

    def stop(self):
        GPIO.output(self.relay_pin, True)


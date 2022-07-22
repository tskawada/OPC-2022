import RPi.GPIO as GPIO
from time import sleep

class Relay:
    def __init__(self):
        self.RELAY_PIN = 17

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RELAY_PIN, GPIO.OUT)

    def straight(self):
        GPIO.output(self.RELAY_PIN, False)

    def stop(self):
        GPIO.output(self.RELAY_PIN, True)

    def __del__(self):
        GPIO.cleanup()

if __name__ == "__main__":
    straight()
    sleep(5)
    print("stop")
    stop()
    GPIO.cleanup()

import RPi.GPIO as GPIO
from time import sleep

RELAY_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def straight():
    GPIO.output(RELAY_PIN, False)

def stop():
    GPIO.output(RELAY_PIN, True)

if __name__ == "__main__":
    straight()
    sleep(5)
    print("stop")
    stop()
    GPIO.cleanup()


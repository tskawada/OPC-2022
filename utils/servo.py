import RPi.GPIO as GPIO
import time
import argparse

parser = argparse.ArgumentParser(description='netcat shell')
parser.add_argument('-a', help='define angle', dest='angle', default=10)

args = parser.parse_args()
print(args)
angle = format(args.angle)
print(angle)

angle = int(angle)

#PWMの設定
Servo_pin = 18
#Relay_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(Servo_pin, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

#サーボモータSG90の周波数は50[Hz]
Servo1 = GPIO.PWM(Servo_pin, 50)
Servo2 = GPIO.PWM(17, 50)

#角度からデューティ比を求める関数
def servo_angle(angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180   #角度からデューティ比を求める
    Servo1.ChangeDutyCycle(duty)     #デューティ比を変更
    time.sleep(0.3)

def servo(value):
    value = value*10
    mod = value % 10
    
    Servo1.start(0) #Servo.start(デューティ比[0-100%])
    Servo2.start(0)
    if(mod != 0 or value > 40 or value < -40):
        print("Your input angle is mistake!!!!")
        print()
    else:
        GPIO.output(17, 1)
        time.sleep(1.0)
        print("test\n")
        servo_angle(value)
        time.sleep(5.0)
    Servo1.stop()
    Servo2.stop()

# #初期化
try:
    servo(angle)
    # GPIO.cleanup()
except:
    print("exception occurs")
    Servo1.stop()
    Servo2.stop() 
    # GPIO.cleanup()
finally:
    GPIO.cleanup()

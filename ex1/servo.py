import RPi.GPIO as GPIO
import time
import argparse

class Servo:
    def __init__():
        parser = argparse.ArgumentParser(description='netcat shell')
        parser.add_argument('-a', help='define angle', dest='angle', default=10)

        args = parser.parse_args()
        # print(args)
        angle = int(format(args.angle))
        # angle = format(args.angle)
        # print(angle)

        # angle = int(angle)

        #PWMの設定
        Servo_pin = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Servo_pin, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)

        #サーボモータSG90の周波数は50[Hz]
        servo = GPIO.PWM(Servo_pin, 50)
    
    def set_angle(value):
        this.servo.start(0)
        servo_angle(value)
        this.servo.stop()

    #角度からデューティ比を求める関数
    def servo_angle(angle):
        duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180   #角度からデューティ比を求める
        this.servo.ChangeDutyCycle(duty)     #デューティ比を変更
        # time.sleep(0.3)

def servo_func(value):
    value = value*10
    mod = value % 10
    
    servo.start(0) #Servo.start(デューティ比[0-100%])
    if(mod != 0 or value > 40 or value < -40):
        print("Your input angle is mistake!!!!")
        print()
    else:
        GPIO.output(17, 1)
        time.sleep(1.0)
        print("test\n")
        servo_angle(value)
        time.sleep(5.0)
    servo.stop()

# #初期化
try:
    servo_func(angle)
except:
    print("exception occurs")
    servo.stop()
finally:
    GPIO.cleanup()
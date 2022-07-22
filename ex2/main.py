from ex2.servo import Servo
from face_detector import FaceDetector
from relay import Relay
from servo import Servo
import cv2

def main():
    fd = FaceDetector()
    servo = Servo()
    relay = Relay()

    while True:
        center_x = fd.get_center_x()

        if center_x is not None:
            relay.straight()

            print(center_x, end="")
            if center_x > fd.cap_width / 2:
                servo.servo_ctrl(-3)
                print("Move right")
            else:
                servo.servo_ctrl(3)
                print("Move left")
        else:
            relay.stop()
            print("No face")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            del fd
            del relay
            del servo
            break
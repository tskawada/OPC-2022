from relay import Relay
from servo import Servo
import cv2


class FaceDetector():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cascade = self.load_cascade()
        self.cap_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.cap_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def load_cascade(self):
        ### 1. カスケードの読み込み ####################################
            # cv2のメソッドを調べて，カスケードファイルを読み込む
        
        cascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_alt2.xml")
        return cascade
        
        ###############################################################

    def detect(self):
        while True:
            ret, img = self.cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.cascade.detectMultiScale(
                gray, 
                scaleFactor=1.1, 
                minNeighbors=3, 
                minSize=(30,30)
            )
            if len(faces) > 0:
                for rect in faces:
                    cv2.rectangle(
                        img, 
                        tuple(rect[0:2]),
                        tuple(rect[0:2]+rect[2:4]), 
                        (0,0,255), 
                        thickness=2
                    )
            cv2.imshow("Face", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    def get_center_x(self):
        ret, img = self.cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=3, 
            minSize=(30,30)
        )
        face = self.biggest_face(faces)
        if face is None:
            return None
        
        ### 2. 顔の中心座標を求める ####################################
            # 顔の中心座標を求め，center_xに代入する

        center_x = face[0] + face[2] / 2

        ###############################################################
        
        return center_x

    def biggest_face(self, faces):
        if len(faces) == 0:
            return None
        biggest = faces[0]

        ### 3. 検出した物体のうち一番大きいものを探す ####################
            # 面積を算出し，一番大きいものをbiggestに代入する
        
        for face in faces:
            if face[2] * face[3] > biggest[2] * biggest[3]:
                biggest = face
        
        ###############################################################
        return biggest

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()


def main():
    fd = FaceDetector()
    servo = Servo()
    relay = Relay()

    while True:
        center_x = fd.get_center_x()

        if center_x is not None:
            relay.straight()

            ### 4. サーボを動かす ##########################################
                # 物体が左にあるときは、サーボを左に動かす
                # 物体が右にあるときは、サーボを右に動かす
                # 物体が中央にあるときは，サーボを中央に動かす

            print(center_x, end="")
            if center_x > fd.cap_width / 2 + 100:
                servo.servo_ctrl(3)
                print("Move right")
            elif center_x < fd.cap_width / 2 - 100:
                servo.servo_ctrl(-3)
                print("Move left")
            else:
                servo.servo_ctrl(0)
                print("Move center")

            ###############################################################
        else:
            relay.stop()
            print("No face")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            del fd
            del relay
            del servo
            break

if __name__ == "__main__":
    main()

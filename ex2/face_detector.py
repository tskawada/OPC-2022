# -*- coding: utf-8 -*-
import cv2

class FaceDetector():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_alt2.xml")

    def detect(self):
        while True:
            ret, img = self.cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
            if len(face) > 0:
                for rect in face:
                    cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=2)
            cv2.imshow("Face", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    fd = FaceDetector()
    fd.detect()

if __name__ == '__main__':
    main()

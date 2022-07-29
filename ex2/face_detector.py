# -*- coding: utf-8 -*-
import cv2

class FaceDetector():
    def __init__(self, cascade):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FPS, 2)
        # self.cascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_alt2.xml")
        self.cascade = cascade
        # self.cap_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        # self.cap_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

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
        return face[0] + face[2] / 2

    def biggest_face(self, faces):
        if len(faces) == 0:
            return None
        biggest = faces[0]
        for face in faces:
            if face[2] * face[3] > biggest[2] * biggest[3]:
                biggest = face
        return biggest

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    fd = FaceDetector()
    fd.detect()

if __name__ == '__main__':
    main()

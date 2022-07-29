# -*- coding: utf-8 -*-
import cv2

def main():
    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_alt2.xml")
    # cascade = cv2.CascadeClassifier("cascade/haarcascade_fullbody.xml")

    while True:
        ret, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

        print(face)
        if len(face) > 0:
            for rect in face:
                cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=2)
        cv2.imshow("Face", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

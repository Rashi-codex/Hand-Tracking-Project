import cv2

import time
import mediapipe as mp
import hand_module as hm


pTime = 0
cTime=0
cap = cv2.VideoCapture(0)
detector = hm.handDetector()

while True:
    success, img = cap.read()

    if not success:
        print("Camera not working")
        break

    img = detector.findHands(img,draw=False)

    lmList = detector.findPostion(img,draw=False)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img,
        str(int(fps)),
        (10, 70),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        (255, 0, 255),
        3
    )

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


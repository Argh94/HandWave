import sys

try:
    import cv2
except ImportError:
    print("خطا: کتابخانه opencv-python نصب نیست. لطفاً با دستور زیر آن را نصب کنید:")
    print("pip install opencv-python")
    sys.exit(1)

try:
    import mediapipe as mp
except ImportError:
    print("خطا: کتابخانه mediapipe نصب نیست. لطفاً با دستور زیر آن را نصب کنید:")
    print("pip install mediapipe")
    sys.exit(1)

import time
import math

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.lmList = []

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            
            if xList and yList:
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                bbox = xmin, ymin, xmax, ymax

                if draw:
                    cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20), (bbox[2] + 20, bbox[3] + 20), (0, 255, 0), 2)
        
        return self.lmList, bbox

    def fingersUp(self):
        fingers = []
        if len(self.lmList) > self.tipIds[0]:
            if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        for id in range(1, 5):
            if len(self.lmList) > self.tipIds[id]:
                if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers

    def findDistance(self, p1, p2, img, draw=True):
        if len(self.lmList) <= max(p1, p2):
            return -1, img, [0, 0, 0, 0, 0, 0]
            
        x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        if draw:
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        
        length = math.hypot(x2 - x1, y2 - y1)
        return length, img, [x1, y1, x2, y2, cx, cy]

def main():
    pTime = 0
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("خطا: نمی‌توان به وب‌کم دسترسی پیدا کرد. لطفاً مطمئن شوید وب‌کم متصل و فعال است.")
        sys.exit(1)
    
    detector = handDetector()
    
    while True:
        success, img = cap.read()
        if not success:
            print("خطا: دریافت فریم از وب‌کم ممکن نیست. لطفاً وب‌کم را بررسی کنید.")
            break
            
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import sys

try:
    import cv2
except ImportError:
    print("خطا: کتابخانه opencv-python نصب نیست. لطفاً با دستور زیر آن را نصب کنید:")
    print("pip install opencv-python")
    sys.exit(1)

try:
    import numpy as np
except ImportError:
    print("خطا: کتابخانه numpy نصب نیست. لطفاً با دستور زیر آن را نصب کنید:")
    print("pip install numpy")
    sys.exit(1)

try:
    import HandTrackingModule as htm
except ImportError:
    print("خطا: ماژول HandTrackingModule یافت نشد. لطفاً مطمئن شوید فایل HandTrackingModule.py در همان پوشه کد قرار دارد.")
    sys.exit(1)

try:
    from ctypes import cast, POINTER
except ImportError:
    print("خطا: کتابخانه ctypes نصب نیست. این کتابخانه معمولاً با پایتون نصب می‌شود. لطفاً پایتون را به‌روزرسانی کنید.")
    sys.exit(1)

try:
    from comtypes import CLSCTX_ALL
except ImportError:
    print("خطا: کتابخانه comtypes نصب نیست. لطفاً با دستور زیر آن را نصب کنید:")
    print("pip install comtypes")
    sys.exit(1)

try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except ImportError:
    print("خطا: کتابخانه pycaw نصب نیست. لطفاً با دستور زیر آن را نصب کنید:")
    print("pip install pycaw")
    sys.exit(1)

import time
import math

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=1)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    if not success:
        print("خطا: نمی‌توان به وب‌کم دسترسی پیدا کرد. لطفاً مطمئن شوید وب‌کم متصل و فعال است.")
        break
    
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        if len(lmList) > 8:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            length = math.hypot(x2 - x1, y2 - y1)
            
            vol = np.interp(length, [50, 300], [minVol, maxVol])
            volBar = np.interp(length, [50, 300], [400, 150])
            volPer = np.interp(length, [50, 300], [0, 100])
            
            if abs(volume.GetMasterVolumeLevel() - vol) > 1:
                volume.SetMasterVolumeLevel(vol, None)

            if length < 50:
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

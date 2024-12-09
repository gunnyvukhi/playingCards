from ultralytics import YOLO
import cv2
import cvzone
import math
import PokerHandFunction
from CaculateWin import CaculateWinRate

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # For webcam use 0 with DirectShow backend
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

model = YOLO("playingCards.pt")
classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']
hand_old = list()
WinRate = ''
result = ''
while True:
    success, img = cap.read()
    if not success:
        break
    results = model(img, stream=True)
    picked = set()
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            if conf < 0.5:
                continue
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            
            # Class Name
            cls = int(box.cls[0])
 
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

            picked.add(classNames[cls])
    
    hand = list(picked)
    if hand != hand_old:
        hand_old = hand
        print(hand)
        if len(hand) > 4:
            WinRate = CaculateWinRate(hand[0:2], hand[2:], 4, 10000)
            result = PokerHandFunction.findPokerHand(hand)
            print(result, WinRate)

    if WinRate and result:
        cvzone.putTextRect(img, f'Your Hand: {result}', (img.shape[1] // 2 - 100, img.shape[0] // 2 - 100), scale=2, thickness=2)
        cvzone.putTextRect(img, f'Win Rate: {WinRate}', (img.shape[1] // 2 - 100, img.shape[0] // 2), scale=2, thickness=2)

    cv2.imshow("Your POV", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
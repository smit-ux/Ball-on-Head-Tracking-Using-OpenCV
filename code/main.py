import cv2
import numpy as np
import imutils
import time,serial
arduino = serial.Serial(port='COM10', baudrate=115200)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    data = arduino.readline()
    return data
# define a video capture object
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
last_time = time.time()
while (True):

    ret, frame = cap.read()
    crop = frame[340:380,0:1280]
    frame = crop
    frame = cv2.blur(frame, (10, 1))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_threshold = cv2.inRange(hsv, (94, 62, 75), (127, 255, 255))
    kernel = np.ones((11, 11), np.float32) / 121
    mask = cv2.morphologyEx(frame_threshold, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(frame_threshold, cv2.MORPH_OPEN, kernel)
    res = cv2.bitwise_and(crop, crop, mask=mask)
    contours, Hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        cv2.drawContours(crop, contours, -1, (0, 255, 0), 5)
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        # draw the biggest contour (c) in green
        cv2.rectangle(crop, (x, y), (x + w, y + h), (255, 0, 0), 2)
        xm = x + w // 2
        ym = y + h // 2
        cv2.circle(crop, (xm, ym), 3, (255, 255, 255), -1)
        angle = (640 - xm)//13.4939759
        dist = 8320//w
        result = str(int(angle))+'a'+str(dist)
        a = write_read(result)
        print(a)
    (h, w) = crop.shape[:2]
    cv2.line(crop, (w // 2, 0), (w // 2, h), (255, 0, 0), 1, 1)  # vertical
    cv2.line(crop, (0, h // 2), (w, h // 2), (0, 255, 0), 1, 1)  # horizontal
    text = f"FPS: {int(1 / (time.time() - last_time))}"
    last_time = time.time()
    cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow('frame', crop)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

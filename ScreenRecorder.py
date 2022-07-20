import numpy as np
import cv2
from win32api import GetSystemMetrics
import pyautogui

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # coder formay
fps = 15
capture_video = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

record_seconds = 100
print('Recording Video')

for i in range(int(record_seconds * fps)):
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    capture_video.write(frame)
    cv2.imshow("screenshot", frame)
    if cv2.waitKey(1) == ord("s"):
        break

cv2.destroyAllWindows()
capture_video.release()
print('Finish')
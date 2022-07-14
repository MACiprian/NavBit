from PIL import ImageGrab
import numpy as np
import cv2
from outcome import capture
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') #coder formay
capture_video = cv2.VideoWriter('output.mp4', fourcc, 40.0, (width, height))

while True:
    img = ImageGrab.grab(bbox = (0, 0, width, height)) #grab image from the screen AND THE RESOLUTION OF THE PROGRAM
    img_np = np.array(img) #converting to np array
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('S.S. Bomb', img_final)
    capture_video.write(img_final) #final image captured
    if cv2.waitKey(10) == ord('s'):
        break
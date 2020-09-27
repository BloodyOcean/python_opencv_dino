import numpy as np
import cv2 as cv
from mss import mss
import mss.tools
import win32api, win32con
import keyboard

keyboard.wait('Alt+1')

while not keyboard.is_pressed('Alt+3'):

    with mss.mss() as sct:

        mon = {'top': 358, 'left': 500, 'width': 25, 'height': 42}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**mon)

        # Grab the data
        sct_img = sct.grab(mon)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

        img = cv.imread(output)

        px = img[0:25, 0:44]
        print(px)

        if(83 in px):

            win32api.keybd_event(win32con.VK_UP, 0, 0, 0)

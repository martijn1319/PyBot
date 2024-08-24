import time
import sys
import random
import webbrowser

firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"

firefox = webbrowser.get(f"'{firefox_path}' %s")

def open_browser(url):
    firefox.open_new_tab(url)

